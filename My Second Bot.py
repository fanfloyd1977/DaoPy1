
from tkinter import *
from gtts import gTTS
import os
import playsound
language = "en"


root=Tk()
def send():
    send = "You : " + e.get()
    txt.insert(END, "\n" +send)
    if (e.get()=="hello" or e.get()=="hi" or e.get()=="Hello", e.get()=="Hi"):
        txt.insert(END,"\n" + "Bot : Hello, there")
        mytext = "Hello, there"
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        #os.system("welcome.mp3")
        playsound.playsound("welcome.mp3", True)

    else:
        txt.insert(END, "\n"+ "Bot : I'm sorry")
        mytext = "I'm sorry"
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("sorry.mp3")
        playsound.playsound("sorry.mp3", True)


    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("My first ChatBot")
root.mainloop()




