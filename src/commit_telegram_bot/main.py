# BDadmehr0.github commit_post_bot main.py 
# Telgram Send message with bot api: https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=<CHAT_ID>&text=<TEXT>
# Using https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx for send mess without proxy, ...
import requests

BOT_TOKEN = "6503477136:AAFSWflzZfODSk9wEW7Jk6XWoJ8AZNH2qVI"
CHANNEL_CHAT_ID = "-1002179618133"
MESSAGE = "Hello World!"

data = {
    'UrlBox': 'https://api.telegram.org/bot6503477136:AAFSWflzZfODSk9wEW7Jk6XWoJ8AZNH2qVI/sendMessage?chat_id=-1002179618133&text=Hell',
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
    return response

send_telegram_mess = send_tel(MESSAGE, BOT_TOKEN, CHANNEL_CHAT_ID)
print(send_telegram_mess)
