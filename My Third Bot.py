"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Dao Dao")
trainer = ListTrainer(chatbot)
trainer.train(["hi, can I help you find a course", "your course have been selected"])

response = chatbot.get_response("I want a course")
print(response)

"""

########################################################################

from tkinter import *
from gtts import gTTS
import os
import playsound
language = "en"

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    "My Bot",
     logic_adapters=["chatterbot.logic.TimeLogicAdapter","chatterbot.logic.MathematicalEvaluation"
    ]
)

#conversation = ["hi", "hello", "Good morning"]

#trainer = ListTrainer(chatbot)
#trainer.train(conversation)



print("\n Ready")

while(True):
    raw = input(">")
    response = chatbot.get_response(raw)
    print(response)

    mytext = str(response)
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("chat.mp3")
    playsound.playsound("chat.mp3")
    os.remove("chat.mp3")