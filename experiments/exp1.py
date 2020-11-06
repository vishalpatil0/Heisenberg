from speech_recognition import Microphone, Recognizer

recog=Recognizer()
mic=Microphone()

with mic:
    print("talk")
    audio=recog.listen(mic)

recognize=recog.recognize_google(audio)

print(recognize)