from flask import Flask, request, abort
import requests
import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi("ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")


#@app.route("/")
#def hello():
#    return "Hello DAO Flask-Heroku"


@app.route("/", methods=["POST", "GET"])
def webhook():
    if request.method == "POST":
        payload = request.json
        Reply_token = payload["event"][0]["replyToken"]
        print(Reply_token)
        message = payload["events"][0]["message"]["text"]
        print(message)
        if "how" in message:
            Reply_message = "Good job"
            ReplyMessage(Reply_token,Reply_message,"ziev+1/ECWJDjw1CkOPjOMofjQ5mft0H0XtZknC/Vu+KnGZzi+2vFVF34UiX+QOdh4JADi+j/xeyPeSiGjyhnvTvKjNijstiixgQeY77aBxJ7R0B8TS/BMCG/y8KheHMwAZ7TJFKN6i5UPBoRzm2BQdB04t89/1O/w1cDnyilFU=")
        return request.json, 200
    else:
        abort(400)

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = "https://api.line.me/v2/bot/message/reply"
    Authorization = "Bearer {}".format(Line_Acees_Token)
    print(Authorization)
    headers = {
        "Content-Type" : "application/json; charset=UTF-8",
        "Authorization":Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }
    data = json.dumps(data)
    r = request.post(LINE_API, headers=headers, data=data)
    return 200


if __name__ == "__main__":
    app.run()

