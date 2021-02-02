import os

from pandas import pandas as pd


from random import randrange
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi("ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")


greeting = ["Hello","Hi", "Hi, Dao :)", "Hi, There!", "Howdy", "สวัสดีครับ"]


emo = ["How are you?", "How r u?",
       "Im fine, Thanks you and you", "I want to fly away", "Someday, I will fly", "I'm doing well", "I miss you"]

address = ["Nanotec thai",
            "ลัพธ์พร วยาจุต ศูนย์นาโนเทคโนโลยีแห่งชาติ (นาโนเทค) 111 อุทยานวิทยาศาสตร์ประเทศไทย ถนน พหลโยธิน ต.คลองหนึ่ง อ.คลองหลวง 12120",
            "Nanotec eng",
            "Dr. Lapporn Vayachuta National Science and Technology Development Agency 111 Thailand Science Park (TSP) Phahonyothin Road, Khlong Nueng, Khlong Luang, Pathum Thani 12120, Thailand",
            "Home non thai",
            "74/74 ชูชาติอนุสรณ์ 7 เลี่ยงเมืองปากเกร็ด 46 ตำบลบางตลาด อำเภอ ปากเกร็ด นนทบุรี 11120",
            "Home non eng",
            "74/74 Chuchat Anuson 7,Liang mueang pak kret 46,Bang Talat, Pak Kret District, Nonthaburi, 11120"]
Miss_Lee = ["Miss Lee", "Shoot me in the heart", "Miss u", "https://www.youtube.com/watch?v=yJCzZqrWIzY"]

Good_Night = ["Good night", "Gnight", "Bye Bye", "Night night....good dream", "Good night ...sleep tight", "Miss you", "Miss u", "Bye"]

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
#Greetings_1
        if event.message.text.lower() in [low.lower() for low in greeting]:
            value = randrange(0, len(greeting))
            reply_text = greeting[value]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Greetings_2
        if event.message.text.lower() == "Name?".lower():
            reply_text = "Hi, I'm Miss Lee. Nice to meet u"
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Greetings_3
        if event.message.text.lower() == greeting[0].lower():
            value = randrange(1, len(greeting))
            reply_text = greeting[value]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Emo_1
        if event.message.text.lower() == emo[0].lower() or event.message.text.lower() == emo[1].lower():
            value = randrange(2, len(emo))
            reply_text = emo[value]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Address_1
        if event.message.text.lower() == address[0].lower():
            reply_text = address[1]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Address_2
        if event.message.text.lower() == address[2].lower():
            reply_text = address[3]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Address_3
        if event.message.text.lower() == address[4].lower():
            reply_text = address[5]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Address_4
        if event.message.text.lower == address[6].lower():
            reply_text = address[7]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Miss Lee
        if event.message.text.lower() == Miss_Lee[0].lower() or event.message.text.lower() == Miss_Lee[1].lower():
            value = randrange(2, len(Miss_Lee))
            reply_text = Miss_Lee[value]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Goodnight

        if  event.message.text.lower() in [low.lower() for low in Good_Night]:
            value = randrange(0, len(Good_Night))
            reply_text = Good_Night[value]
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
#Image
        if event.message.text.lower() == "send image":
            reply_text = "https://www.pinterest.com/pin/88875792631945830/"
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))



        else:
            data = pd.read_excel(r"Book.xls")
            row = data.shape[0]
            for i in range(row):
                 if event.message.text.lower() == data["Question"].values[i]:
                    reply_text = data["Answer"].values[i]
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text))
            else:
                reply_text = "ok"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text))


if __name__ == "__main__":
    app.run()