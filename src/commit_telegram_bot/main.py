# BDadmehr0.github commit_post_bot main.py 
# Telgram Send message with bot api: https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=<CHAT_ID>&text=<TEXT>
# Using https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx for send mess without proxy, ...

BOT_TOKEN = "6503477136:AAFSWflzZfODSk9wEW7Jk6XWoJ8AZNH2qVI"
CHANNEL_CHAT_ID = "-1002179618133"
MESSAGE = "Hello World!"

# send message to ch telegram
def send_tel(mess, bot_token, chat_id):
    return mess, bot_token, chat_id

send_telegram_mess = send_tel(MESSAGE, BOT_TOKEN, CHANNEL_CHAT_ID)
print(send_telegram_mess)
