import os
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi("1655584117")
handler = WebhookHandler("4088552f2e9ee28de065d9bddce75ab2")
user_profile = "far"

@app.route("/")

def hello():
    return "Hello DAO Flask-Heroku"

@app.route("/", methods=['GET'])
def home():
    profile = line_bot_api.get_profile(user_profile)

    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)
    print(profile.status_message)
    return '<div><h1>ok</h1></div>'

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body:" + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.push_message(
        event.reply_token,
        TextSendMessage(text="hello world"))


if __name__ == "__main__":
    app.run()
