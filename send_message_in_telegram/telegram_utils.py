import requests
from secret import secret_keys

def send_message_to_chat(chat_id, message):
    """
    Function will send message to a telegram channel, read the docs to setup
    Args:
        chat_id : the chat id of the channel, see docs to get the chat id
        message : the message to be send to the chat
    Returns:
        status code
    """

    url = "https://api.telegram.org/bot{bot_api_key}/sendMessage".format(bot_api_key = secret_keys.TELEGRAM_BOT_API_KEY)

    data = {'chat_id' : chat_id,
            'text' : message}

    response = requests.post(url, data = data)

    return response.status_code
