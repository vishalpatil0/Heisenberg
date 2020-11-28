import pyttsx3
import speech_recognition as sr
import datetime,wikipedia,webbrowser,os,random,requests,pyautogui,playsound,subprocess,time
import urllib.request,bs4 as bs,sys
import mini,wolframalpha
import StonePaperScissor as SPS

"""Setting variables"""
try:
    app=wolframalpha.Client("JPK4EE-L7KR3XWP9A")
except Exception as e:
    pass

#setting chrome path
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
    while(True):
        query=takeCommand().lower()
        
        #wikipedia search 
        if there_exists(['wikipedia'],query):
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
           
        elif there_exists(["what is your name","what's your name","tell me your name"],query):
            speak("My name is Jarvis and i'm here to serve you.")

        #google, youtube and location
        elif there_exists(['open youtube','access youtube'],query):
            speak("Opening youtube")
            webbrowser.get(chrome_path).open("https://www.youtube.com")
        elif there_exists(['open google and search','google and search'],query):
            url='https://google.com/search?q='+query[query.find('for')+4:]
            webbrowser.get(chrome_path).open(url)
        elif there_exists(['open google'],query):
            speak("opening google")
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

        #play music 
        elif there_exists(['play music'],query):
            speak("Playing musics")
            music_dir='D:\\Musics\\vishal'
            songs=os.listdir(music_dir)
            # print(songs)
            indx=random.randint(0,50)
            os.startfile(os.path.join(music_dir,songs[indx]))

        #play game
        elif there_exists(['would like to play some games','want to play games','play games','open games','play game','open game'],query):
            speak("We have only one game right now")
            speak("Stone Paper Scissor")
            speak("opening stone paper scissor")
            SPS.start()

        #makig note
        elif there_exists(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
            speak("What would you like to write down?")
            data=takeCommand()
            n=mini.note()
            n.Note(data)
            speak("I have a made a note of that.")

        #flipping coin
        elif there_exists(["toss a coin","flip a coin","toss"],query):
            moves=["head", "tails"]
            cmove=random.choice(moves)
            playsound.playsound('quarter spin flac.mp3')
            speak("It's " + cmove)

        #time and date
        elif there_exists(['the time'],query):
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif there_exists(['the date'],query):
            strDay=datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {strDay}")

        #opening software applications
        elif there_exists(['open chrome'],query):
            speak("Opening chrome")
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            time.sleep(5)
        elif there_exists(['open notepad plus plus','open notepad++','open notepad ++'],query):
            speak('Opening notepad++')
            os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
            time.sleep(3)
        elif there_exists(['open notepad','start notepad'],query):
            speak('Opening notepad')
            os.startfile(r'C:\Windows\notepad.exe')
            time.sleep(3)
        elif there_exists(['open code','open visual studio ','open vs code'],query):
            speak("Opeining vs code")
            codepath=r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
            time.sleep(4)
        elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc'],query):
            speak("Opening File Explorer")
            os.startfile("C:\Windows\explorer.exe")
            time.sleep(3)
        elif there_exists(['powershell'],query):
            speak("opening powershell")
            os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
            time.sleep(4)
        elif there_exists(['whatsapp'],query):
            speak("opening whatsApp")
            os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
            time.sleep(7)
        elif there_exists(['open vlc','vlc media player','vlc player'],query):
            speak("Opening VLC media player")
            os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
            time.sleep(5)

        #screeshot
        elif there_exists(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
            speak("Taking screenshot")
            m2=mini.screenshot()
            m2.takeSS()
            speak('Captured screenshot is saved in Screenshots folder.')

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
        elif there_exists(['+','-','*','x','/','plus','add','minus','subtract','divide','multiply','divided','multiplied'],query):
            try:
                res=app.query(query)
                speak(next(res.results).text)
            except:
                print("Internet Connection Error")
            
        #shutting down system
        elif there_exists(['exit','quit','shutdown','shut up','goodbye','shut down'],query):
            speak("shutting down")
            sys.exit()
        
        elif there_exists(['none'],query):
            pass
        #it will give online results for the query
        else:
            try:
                res=app.query(query)
                speak(next(res.results).text)
            except:
                print("Internet Connection Error")


