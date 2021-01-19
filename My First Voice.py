from gtts import gTTS

import os

mytext = "ก้อนฆ่าเชื้อ คิวบ์-เอ็กซ์"
language = "th"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
