from gtts import gTTS
import time
import os
import playsound
print(time.ctime())
tts=gTTS("What is the cost of lies?", lang='en')
a='ok.mp3'
tts.save(a)
playsound.playsound(a)
os.remove(a)
