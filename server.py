from flask import Flask, request
from threading import Thread
import telegrambot
import pandas as pd
from tabulate import tabulate
import json

app = Flask(__name__)
@app.route('/webhook', methods=['POST', 'GET'])
def post_message():
  try:
    jsonRequest = request.args.get("jsonRequest", default="false").lower()  
    if request.method == 'POST':
        if jsonRequest == "true":
            payload = request.get_json()  # Safely get JSON data
            payload = json.dumps(payload, indent=4) if payload is not None else 'No JSON payload'
        else:
            payload = request.data.decode('utf-8')  # Decode bytes to string
        print("Received data:\n", payload)
        telegrambot.sendMessage(payload)  
        return 'Success', 200
    else:
        print("GET request")
        return 'Success', 200
  except Exception as e:
    print("[X] Exception Occured : ", e)
    return 'failure', 500

@app.route('/')
def main():
  return 'Your bot is alive!'

def run():
  app.run(host='0.0.0.0', port=5000)


def start_server_async():
  server = Thread(target=run)
  server.start()

def start_server():
  app.run(host='0.0.0.0', port=5000)