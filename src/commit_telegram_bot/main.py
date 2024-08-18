import requests
from bs4 import BeautifulSoup

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

def ex_data_github():
    return True

def send_tel(mess, bot_token, chat_id):
    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response

send_telegram_mess = send_tel(MESSAGE, BOT_TOKEN, CHANNEL_CHAT_ID)
print(send_telegram_mess)

