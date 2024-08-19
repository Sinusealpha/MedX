# last commit data API: https://api.github.com/repos/Sinusealpha/MedX/branches/master
import requests

BOT_TOKEN = "6503477136:AAFSWflzZfODSk9wEW7Jk6XWoJ8AZNH2qVI"
CHANNEL_CHAT_ID = "-1002179618133"
MESSAGE = "HelloWorld!"



def send_tel(mess, bot_token, chat_id):
    # httpdebugger Data
    data = {
        'UrlBox': f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={mess}',
        'ContentTypeBox': '',
        'ContentDataBox': '',
        'HeadersBox': '',
        'RefererBox': '',
        'AgentList': 'Internet Explorer',
        'AgentBox': '',
        'VersionsList': 'HTTP/1.1',
        'MethodList': 'GET',
    }

    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response


# send_telegram_mess = send_tel(MESSAGE, BOT_TOKEN, CHANNEL_CHAT_ID)
# print(send_telegram_mess, extracted_data)
