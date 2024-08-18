# BDadmehr0.github commit_post_bot main.py 
# Telgram Send message with bot api: https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=<CHAT_ID>&text=<TEXT>
# Using https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx for send mess without proxy, ...
import requests

# Telegram & Bot data
BOT_TOKEN = "6503477136:AAFSWflzZfODSk9wEW7Jk6XWoJ8AZNH2qVI"
CHANNEL_CHAT_ID = "-1002179618133"
MESSAGE = "HelloWorld!"

# httpdebugger Data
data = {
    'UrlBox': f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_CHAT_ID}&text={MESSAGE}',
    'ContentTypeBox': '',
    'ContentDataBox': '',
    'HeadersBox': '',
    'RefererBox': '',
    'AgentList': 'Internet Explorer',
    'AgentBox': '',
    'VersionsList': 'HTTP/1.1',
    'MethodList': 'GET',
}

# send message to ch telegram
def send_tel(mess, bot_token, chat_id):
    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response, response.text

send_telegram_mess = send_tel(MESSAGE, BOT_TOKEN, CHANNEL_CHAT_ID)
print(send_telegram_mess)
