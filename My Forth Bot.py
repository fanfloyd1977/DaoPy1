from gtts import gTTS
import os
import playsound
language = "en"



from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



chatbot = ChatBot("My Bot")
trainer = ListTrainer(chatbot)

chatbot.storage.drop()




trainer.train(["Hi there", "Hello"])
trainer.train(["hi Dao", "I'm fine, thank you, and you?"])
trainer.train(["Greetings", "Hello!"])
trainer.train(["Who are you?", "I am Dan"])
trainer.train(["สวัสดีค่ะ", "สวัสดีค่ะ สบายดีมั้ยคะ"])
trainer.train(["ชื่ออะไรคะ", "ชื่อดาวค่ะ"])
trainer.train(["I would like to know about CUBE-X", "CUBE-X is a product of Thailand created by Nanotec"])
trainer.train(["tell me about CUBE-X", "Cubic hybrids mesoporous structure for antimicrobial on surfaces"])


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




