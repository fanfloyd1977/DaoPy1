from tkinter import *
from gtts import gTTS
import os
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello My first smart pop-up"





