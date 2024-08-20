import requests
import json

# Define the bot token and the channel chat ID for sending messages via Telegram
BOT_TOKEN = "<TELEGRAM_BOT_TOKEN>"
CHANNEL_CHAT_ID = "<TELEGRAM_CH_ID>"

# URL to access the GitHub API for the specific repository's commits
REPO_URL_API = 'https://api.github.com/repos/<AUTHOR_NAME>/<REPO_NAME>/commits'

# Personal GitHub token for authentication
GITHUB_TOKEN = '<GITHUB_TOKEN>'

def recive_last_commit_data(repo_url_api, github_token):
    """
    Fetches the most recent commit data from the specified GitHub repository.

    :param repo_url_api: The API endpoint for the repository's commits.
    :param github_token: The GitHub token for authentication.
    :return: The most recent commit data as a dictionary, or None if no commits are found.
    """
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    response = requests.get(repo_url_api, headers=headers)
    commits = response.json()

    if commits:
        return commits[0]  # Returning the latest commit
    else:
        return None  # If no commits are found, return None

def save_json_to_file(data, filename):
    """
    Saves the provided data to a JSON file.

    :param data: The data to be saved.
    :param filename: The name of the file to save the data in.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def extract_important_info(commit_data):
    """
    Extracts important information from the commit data.
    
    :param commit_data: A dictionary containing the commit data.
    :return: A dictionary with the extracted information.
    """
    important_info = {
        "sha": commit_data.get("sha"),
        "author_name": commit_data["commit"]["author"].get("name"),
        "author_email": commit_data["commit"]["author"].get("email"),
        "message": commit_data["commit"].get("message"),
        "commit_url": commit_data.get("html_url")
    }
    return important_info

def format_message(info):
    """
    Formats the extracted information into a message suitable for Telegram.
    
    :param info: A dictionary containing the extracted information.
    :return: A formatted string.
    """
    message = (
        f"New commit detected!\n"
        f"SHA: {info['sha']}\n"
        f"Author: {info['author_name']} ({info['author_email']})\n"
        f"Message: {info['message']}\n"
        f"View Commit: {info['commit_url']}\n"
    )
    return message

def send_tel(mess, bot_token, chat_id):
    """
    Sends a message to a specified Telegram channel using the Telegram Bot API.

    :param mess: The message to be sent.
    :param bot_token: The bot token for authentication with the Telegram API.
    :param chat_id: The chat ID of the channel where the message will be sent.
    :return: The response from the HTTP request.
    """
    data = {
        'UrlBox': f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={mess}',  # The full URL for the Telegram API request
        'ContentTypeBox': '',
        'ContentDataBox': '',
        'HeadersBox': '',
        'RefererBox': '',
        'AgentList': 'Internet Explorer',  # User-agent setting for the HTTP request
        'AgentBox': '',
        'VersionsList': 'HTTP/1.1',  # HTTP version
        'MethodList': 'GET',  # HTTP method
    }
    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response

# Fetch the last commit data from the GitHub repository
last_commit_data = recive_last_commit_data(REPO_URL_API, GITHUB_TOKEN)

if last_commit_data:
    # Save the commit data to a JSON file
    save_json_to_file(last_commit_data, 'data.json')
    print(f"Last commit data saved to 'data.json'")  # Print a success message
    
    # Extract the important information from the last commit data
    important_info = extract_important_info(last_commit_data)
    
    # Format the extracted information into a message
    telegram_message = format_message(important_info)
    
    # Send the formatted message to the Telegram channel
    response = send_tel(telegram_message, BOT_TOKEN, CHANNEL_CHAT_ID)
    print("Message sent to Telegram channel")
else:
    print("No commits found.")

