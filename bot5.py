import time
import schedule

from pandas import pandas as pd

from random import randrange
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

#Bot MsLee_DF
line_bot_api = LineBotApi("WJF5U6RE3Or4hvhkrud74QlPwWLWchHlHh/H78fXK37soXeRQ403EGSQ+XNoiHgtNa0k2HpiZhGGofPbU6FD4Bol11nk266Ems7CE7A492ayiM2UefXRKqrcJzWtglydLHQaG9n4nZG7AxsoDIYY3wdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4f7e8072521893ec7cc87056f203cb28")

#Goole sheet Key

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('fanfloyd1977-2bf294ca8a0e.json', scope)
client = gspread.authorize(creds)

#Intent
greeting = ["Hello Hello","Hi Hi", "Hi", "Hi, there", "Good day", "สวัสดีครับ", "สวัสดีค่ะ"]

@app.route("/")
def hello():
    return "Hello DAO Flask-Heroku"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #Intent greeting
    if event.message.text.lower() in [low.lower() for low in greeting]:
        value = randrange(0, len(greeting))
        reply_text = greeting[value]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))

"""

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    for r in greeting:
        res = [j for j in r if any(k.casefold() in j.casefold() for k in event.message.text.lower())]
        if res:
            #value = randrange(6, 7)
            #reply_text = greeting[value]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="สวัสดีค่ะ เรามีสินค้าดังนี้ค่ะ"))

