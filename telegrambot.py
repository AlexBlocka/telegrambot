import os
import requests
from telegram import Bot


def sendMessage(data):
    channel = os.environ['CHANNEL']
    url = f"https://api.telegram.org/bot{os.environ['TOKEN']}/sendMessage"
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    payload = {
        "chat_id": channel,
        "text": data,
    }
    response = requests.post(url, headers=headers, json=payload)
    print('--->Sending message to Telegram:', response.text.encode('utf-8').decode('utf-8'))
    return response.ok