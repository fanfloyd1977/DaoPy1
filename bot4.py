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

    elif event.message.text.lower() == "box":

        buttons_template = ButtonsTemplate(
            title="Miss Lee's box", text="Hello, Miss Dao",actions=[
            PostbackAction(label='start', data='start'),
            PostbackAction(label='end', data='end'),
            DatetimePickerAction(label='show', data='show', mode='date'),
            PostbackAction(label='del', data='del'),
                ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)

#Book
    else:
        sheet = client.open("Bookone").sheet1
        for k in range(2,21):
            sheet.update_cell(k,3,0)
        for j in range(1,21):
            match = 0
            for i in event.message.text.split():
                cell_split = sheet.cell(j,1).value.split()
                if i in cell_split:
                    match +=1
                    sheet.update_cell(j,3,match)
                    time.sleep(1)

        Col_data = sheet.col_values(3)
        M = max(Col_data)
        A = sheet.cell(Col_data.index(M)+1,2).value
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=A))

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    if data == "start":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Test Box"))


if __name__ == "__main__":

    app.run()





