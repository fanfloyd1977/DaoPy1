import os
from random import randrange
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi("ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")

greeting = ["Hello",
            "Hi, Dao :)", "Hi, There!", "Howdy", "สวัสดีครับ"]
value1 = randrange(1, len(greeting))

emo = ["How are you?", "how r u?",
       "Im fine, Thanks you and you", "I want to fly away", "Someday, I will fly", "I'm doing well", "I miss you"]
value2 = randrange(2, len(emo))



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

        if event.message.text == "Hi":
            reply_text = "Hi Dao"
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
        if event.message.text == "Name?":
            reply_text = "Hi, I'm Miss Lee. Nice to meet u"
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
        if event.message.text == greeting[0]:
            reply_text = greeting[value1]
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text))
        if event.message.text == emo[0] or event.message.text == emo[1]:
            reply_text = emo[value2]
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text))




if __name__ == "__main__":
    app.run()