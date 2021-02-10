from pandas import pandas as pd

from random import randrange
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

line_bot_api = LineBotApi("ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('fanfloyd1977-2bf294ca8a0e.json', scope)
client = gspread.authorize(creds)

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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

#Image
    if event.message.text.lower() == "send image":
        image = pd.read_excel(r"Image.xls")
        row = image.shape[0]
        value = randrange(1, row)
        reply_text = image["Url"].values[value]
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url= reply_text, preview_image_url= reply_text))
#Sticker
    if event.message.text.lower() in "send me sticker" or event.message.text.lower() in ["^^", ":)", ";)", "\^o^/"]:
        value = randrange(180, 259)
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(package_id=3, sticker_id=value))

#Book
    else:
        sheet = client.open("Bookone").sheet1

        for k in range(2,15):
            sheet.update_cell(k,3,0)

        for j in range(1,15):
            match = 0
            for i in event.message.text.split():
                if i in sheet.cell(j,1).value.split():
                    match = match+1
                    sheet.update_cell(j,3,match)
                    A = sheet.cell(j,2).value
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(A))


if __name__ == "__main__":
    app.run()