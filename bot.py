import os
from flask import Flask, jsonify, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

app = Flask(__name__)

@app.route("/webhook", methods=['GET', 'POST'])


def webhook():
    if request.method == "POST":
        return "OK"

def hello():
    return "Hello DAo DAo World!"

if (__name__ == "__main__"):
    app.run()