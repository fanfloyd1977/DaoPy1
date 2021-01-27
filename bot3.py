import os
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer

app = Flask(__name__)

line_bot_api = LineBotApi("ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")

"""
chatbot = ChatBot("Miss Lee")
trainer = ListTrainer(chatbot)


trainer.train(["Hi there", "Hello"])
trainer.train(["hi Dao", "I'm fine, thank you, and you?"])
trainer.train(["Greetings", "Hello!"])
trainer.train(["Who are you?", "I am Dan"])
trainer.train(["สวัสดีค่ะ", "สวัสดีค่ะ สบายดีมั้ยคะ"])
trainer.train(["ชื่ออะไรคะ", "ชื่อดาวค่ะ"])
trainer.train(["I would like to know about CUBE-X", "CUBE-X is a product of Thailand created by Nanotec"])
trainer.train(["tell me about CUBE-X", "Cubic hybrids mesoporous structure for antimicrobial on surfaces"])

"""


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
        )


if __name__ == "__main__":
    app.run()
