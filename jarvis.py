import pyttsx3
import speech_recognition as sr 
import datetime,wikipedia,webbrowser,os,random,requests,pyautogui,playsound,subprocess
import urllib.request,bs4 as bs,sys
import mini,wolframalpha

"""Setting variables"""
try:
    app=wolframalpha.Client("JPK4EE-L7KR3XWP9A")
except Exception as e:
    pass

chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
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

def there_exists(terms,query):
    for term in terms:
        if term in query:
            return True

def gen():
    for i in range(1,1001):
        yield i

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>18 and hour<21:
        speak("Good Evening!")
    else:
        speak("It is a beautiful night.")
    speak("I am jarvis sir. How may I help you.")

def speak(audio):
    """It speaks the audio"""
    print(audio)
    engine.say(audio)
    # engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
    # engine.stop()

def takeCommand():
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


if __name__=="__main__":
    # greet()
    """Logic for execution task based on query"""
    g=gen()
    while(True):
        query=takeCommand().lower()
        if there_exists(['wikipedia'],query):
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif there_exists(["what is your name","What's your name","tell me your name"],query):
            speak("My name is Jarvis and i'm here to serve you.")
        elif there_exists(['open youtube','access youtube'],query):
            webbrowser.get(chrome_path).open("https://www.youtube.com")
        elif there_exists(['open google and search','google and search'],query):
            url='https://google.com/search?q='+query[query.find('for')+4:]
            webbrowser.get(chrome_path).open(url)
        elif there_exists(['open google'],query):
            webbrowser.get(chrome_path).open("https://www.google.com")
        elif there_exists(['find location of'],query):
            url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
            webbrowser.get(chrome_path).open(url)
        elif there_exists(["what is my exact location","What is my location","my current location"],query):
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
        elif there_exists(["where am i"],query):
            Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
            loc = Ip_info['region']
            speak(f"You must be somewhere in {loc}")  
        elif there_exists(['play music'],query):
            music_dir='D:\\Musics\\vishal'
            songs=os.listdir(music_dir)
            # print(songs)
            indx=random.randint(0,50)
            os.startfile(os.path.join(music_dir,songs[indx]))
        elif there_exists(['make a note','make note','remember this as note','open notepad and write'],query):
            speak("What would you like to write down?")
            data=takeCommand()
            n=mini.note()
            n.Note(data)
            speak("I have a made a note of that.")
        elif there_exists(["toss a coin","flip a coin","toss"],query):
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            playsound.playsound('quarter spin flac.mp3')
            speak("It's " + cmove)
        elif there_exists(['the time'],query):
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")     
        elif there_exists(['the date'],query):
            strDay=datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {strDay}")
        elif there_exists(['open code','open visual studio ','open vs code'],query):
            codepath=r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        elif there_exists(['powershell'],query):
            os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
        elif there_exists(['whatsapp'],query):
            os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
        elif there_exists(['take screenshot','capture my screen'],query):
            img_captured=pyautogui.screenshot()
            a=os.getcwd()
            os.mkdir("Screenshots")
            os.chdir(a+'\Screenshots')
            img_captured.save("Screenshot"+str(g.__next__())+".png")
            os.chdir(a)
        # elif there_exists(["plus","minus","multiply","divide","power","+","-","*","/"],query):
        #     opr = query.split()[1]

        #     if opr == '+' or 'plus':
        #         speak(int(query.split()[0]) + int(query.split()[2]))
        #     elif opr == '-' or 'minus':
        #         speak(int(query.split()[0]) - int(query.split()[2]))
        #     elif opr == 'multiply' or 'x':
        #         speak(int(query.split()[0]) * int(query.split()[2]))
        #     elif opr == 'divide' or '/':
        #         speak(int(query.split()[0]) / int(query.split()[2]))
        #     elif opr == 'power' or '^':
        #         speak(int(query.split()[0]) ** int(query.split()[2]))
        #     else:
        #         speak("Wrong Operator")
        elif there_exists(['temperature'],query):
            try:
                res=app.query(query)
                speak(next(res.results).text)
            except:
                print("Internet Connection Error")
        elif there_exists(['+','-','*','/','plus','add','minus','subtract','divide','multiply'],query):
            try:
                res=app.query(query)
                speak(next(res.results).text)
            except:
                print("Internet Connection Error")
        elif there_exists(['exit','quit','shutdown','shut up','goodbye'],query):
            sys.exit()
        else:
            sys.exit()
    
