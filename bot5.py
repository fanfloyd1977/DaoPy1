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
line_bot_api = LineBotApi("ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#Intent greeting
    if event.message.text.lower() in [low.lower() for low in greeting]:
        value = randrange(0, len(greeting))
        reply_text = greeting[value]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Flex message
    if event.message.text.lower() == "flex":
        bubble = BubbleContainer(
        direction='ltr',
        hero=ImageComponent(
            url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
            size='full',
            aspect_ratio='20:13',
            aspect_mode='cover',
            action=URIAction(uri='http://example.com', label='label')
        ),
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(text="Brown Cafe",weight="bold",size="xl"),
                BoxComponent(
                    layout="baseline",margin="md",
                    contents=[

                        IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                        TextComponent(text="250 BHT",size="sm",color="#976608",margin="md"),
                        TextComponent(text="450 kcl",size="sm",color="#976608",margin="md",align="end")

                    ]
                ),
                BoxComponent(
                    layout="baseline",margin="md",
                    contents=[
                        IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                        TextComponent(text="450 BHT",size="sm",color="#976608",margin="md"),
                        TextComponent(text="750 kcl",size="sm",color="#976608",margin="md",align="end")

                    ]

                ),
                BoxComponent(
                    layout="vertical",margin="md",
                    contents=[TextComponent(text="Sauce, Onions, Pickles, lettuce & Cheese",size="xxs",color="#999999",margin="md"),]
                )
            ]
        ),
        footer=BoxComponent(
            layout="vertical",spacing="sm",
            contents=[
                ButtonComponent(
                    style="link",
                    height="sm",
                    action=PostbackAction(label="ORDER", data="Ordered")
                    # URIAction(label="ORDER",uri="tel:00000000")
                )
            ]
        )
    )

    message = FlexSendMessage(alt_text="Hello Flex", contents=bubble)
    line_bot_api.reply_message(event.reply_token,message)



@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    if data == "Ordered":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="The order has been submitted"))
        sheet = client.open("Booktwo").sheet1
        N_order = sheet.cell(2,5).value
        N_order +=1
        sheet.update_cell(2,5,N_order)

