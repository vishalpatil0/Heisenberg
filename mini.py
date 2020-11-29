import datetime,subprocess,os,pyautogui,string,random
import pyttsx3
import speech_recognition as sr

class SpeakRecog:
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    # print(voices[].id)
    # print(voices)

    """ VOICE RATE"""
    rate = engine.getProperty('rate')               # getting details of current speaking rate
    # print(rate)
    engine.setProperty('rate', 170)                 # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')           #getting to know current volume level (min=0 and max=1)
    # print(volume)                                 #printing current volume level
    engine.setProperty('volume', 1.0)               # setting up volume level  between 0 and 1
    
    def speak(self,audio):
        """It speaks the audio"""
        print(audio)
        self.engine.say(audio)
        # engine.save_to_file('Hello World', 'test.mp3')
        self.engine.runAndWait()
        # engine.stop()

    def takeCommand(self):
        """It take microphone input from the user and return string"""
        recog=sr.Recognizer()
        # mic=Microphone()
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            print("Listening....")
            recog.pause_threshold = 1
            # r.energy_threshold = 45.131829621150224
            # print(sr.Microphone.list_microphone_names())
            #print(r.energy_threshold)
            audio=recog.listen(source)
        try:
            print("Recognizing...")
            query= recog.recognize_google(audio)
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return 'None'
        return query

class note:
    def Note(self,data):
        date=datetime.datetime.now()
        filename=str(date).replace(':','-')+'-note.txt'
        a=os.getcwd()
        if not os.path.exists('Notes'):
            os.mkdir('Notes')
        os.chdir(a+r'\Notes')
        with open(filename,'w') as f:
            f.write(data)
        subprocess.Popen(['notepad.exe',filename])
        os.chdir(a)

class screenshot:
    def takeSS(self):
        img_captured=pyautogui.screenshot()
        a=os.getcwd()
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
        os.chdir(a+'\Screenshots')
        date=datetime.datetime.now()
        img_captured.save('screenshot-'+str(date).replace(':','-')+'.png')
        os.chdir(a)  

class PasswordGenerator:
    def givePSWD(self):
        SR=SpeakRecog()
        SR.speak("What type of password you want")
        print("\nPassword Level we have:-\n\nPoor Level\nAverage Level\nStrong Level\n")
        while(True):
            query=SR.takeCommand().lower()
            if ('poor' in query):
                return "Your Password is = "+"".join(random.sample(string.ascii_letters,7))
                break
            elif ('average' in query):
                return "Your Password is = "+"".join(random.sample(string.ascii_letters+string.digits,7))
                break
            elif ('strong' in query):
                return "Your Password is = "+"".join(random.sample(string.ascii_letters+string.digits+string.punctuation,7))
                break
            else:
                SR.speak("Please say it again")        