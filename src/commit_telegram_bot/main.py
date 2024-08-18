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

# URL for the GitHub commits page
GITHUB_URL = "https://github.com/Sinusealpha/MedX/commits/main/"

def ex_data_github():
    # Fetch the content from GitHub commits page
    response = requests.get(GITHUB_URL)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract all commit links (modify as needed)
    commit_links = soup.find_all('a', class_='commit-tease-sha')
    extracted_data = [link.get('href') for link in commit_links]

    # Log or print extracted data (for debugging)
    print("Extracted Data:", extracted_data)
    
    # Optionally, send extracted data via Telegram
    if extracted_data:
        message = f"Extracted Commit Links:\n" + "\n".join(extracted_data)
        send_tel(message, BOT_TOKEN, CHANNEL_CHAT_ID)
    
    return extracted_data

def send_tel(mess, bot_token, chat_id):
    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response

send_telegram_mess = send_tel(MESSAGE, BOT_TOKEN, CHANNEL_CHAT_ID)
print(send_telegram_mess)