"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot("Da Da")

conversation = ["Hello", "Hi there!"]
trainer = ListTrainer(chatbot)
trainer.train(conversation)

response = chatbot.get_response("Good Morning")
print(response)

####################################

bot = ChatBot("Test")
conv = open("chats.txt", "r").readline()

#bot.set_trainer(ListTrainer)
bot.train(conv)


while True:
    request = input("you ; ")
    response = bot.get_response(request)
    print("Bot: ", response)



from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#creating a new chatbot
chatbot = ChatBot("Edureka")
trainer = ListTrainer(chatbot)
trainer.train(["hi, can I help you find a course", "sure I'd love to find you a course", "your course have been selected"])

#getting a response from the chatbot
response = chatbot.get_response("I want a course")
print(response)

"""
import winsound
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#creating a new chatbot
chatbot = ChatBot("Edureka")
trainer = ListTrainer(chatbot)
trainer.train(["hi, can I help you find a course", "sure I'd love to find you a course", "your course have been selected"])

while True:
    request = input("you ; ")
    response = chatbot.get_response(request)
    print("Bot: ", response)

