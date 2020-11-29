import datetime,wikipedia,webbrowser,os,random,requests,pyautogui,playsound,subprocess,time
import urllib.request,bs4 as bs,sys
import mini,wolframalpha
import StonePaperScissor as SPS

m2=mini.SpeakRecog()


"""Setting variables"""
try:
    app=wolframalpha.Client("JPK4EE-L7KR3XWP9A")
except Exception as e:
    pass

#setting chrome path
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def there_exists(terms,query):
    for term in terms:
        if term in query:
            return True

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour<12:
        m2.speak("Good Morning!")
    elif hour>=12 and hour<18:
        m2.speak("Good Afternoon!")
    elif hour>18 and hour<21:
        m2.speak("Good Evening!")
    else:
        m2.speak("It is a beautiful night.")
    m2.speak("I am jarvis sir. How may I help you.")

if __name__=="__main__":
    greet()
    """Logic for execution task based on query"""
    while(True):
        query=m2.takeCommand().lower()
        
        #wikipedia search 
        if there_exists(['wikipedia'],query):
            m2.speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            m2.speak("According to wikipedia")
            m2.speak(results)
           
        elif there_exists(["what is your name","what's your name","tell me your name"],query):
            m2.speak("My name is Jarvis and i'm here to serve you.")

        #google, youtube and location
        elif there_exists(['open youtube','access youtube'],query):
            m2.speak("Opening youtube")
            webbrowser.get(chrome_path).open("https://www.youtube.com")
        elif there_exists(['open google and search','google and search'],query):
            url='https://google.com/search?q='+query[query.find('for')+4:]
            webbrowser.get(chrome_path).open(url)
        elif there_exists(['open google'],query):
            m2.speak("opening google")
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
            m2.speak(f"You must be somewhere in {loc}")

        #play music 
        elif there_exists(['play music'],query):
            m2.speak("Playing musics")
            music_dir='D:\\Musics\\vishal'
            songs=os.listdir(music_dir)
            # print(songs)
            indx=random.randint(0,50)
            os.startfile(os.path.join(music_dir,songs[indx]))

        #play game
        elif there_exists(['would like to play some games','want to play games','play games','open games','play game','open game'],query):
            m2.speak("We have only one game right now")
            m2.speak("Stone Paper Scissor")
            m2.speak("opening stone paper scissor")
            SPS.start()

        #makig note
        elif there_exists(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
            m2.speak("What would you like to write down?")
            data=m2.takeCommand()
            n=mini.note()
            n.Note(data)
            m2.speak("I have a made a note of that.")

        #flipping coin
        elif there_exists(["toss a coin","flip a coin","toss"],query):
            moves=["head", "tails"]
            cmove=random.choice(moves)
            playsound.playsound('quarter spin flac.mp3')
            m2.speak("It's " + cmove)

        #time and date
        elif there_exists(['the time'],query):
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            m2.speak(f"Sir, the time is {strTime}")
        elif there_exists(['the date'],query):
            strDay=datetime.date.today().strftime("%B %d, %Y")
            m2.speak(f"Today is {strDay}")

        #opening software applications
        elif there_exists(['open chrome'],query):
            m2.speak("Opening chrome")
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            time.sleep(5)
        elif there_exists(['open notepad plus plus','open notepad++','open notepad ++'],query):
            m2.speak('Opening notepad++')
            os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
            time.sleep(3)
        elif there_exists(['open notepad','start notepad'],query):
            m2.speak('Opening notepad')
            os.startfile(r'C:\Windows\notepad.exe')
            time.sleep(3)
        elif there_exists(['open code','open visual studio ','open vs code'],query):
            m2.speak("Opeining vs code")
            codepath=r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
            time.sleep(4)
        elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc'],query):
            m2.speak("Opening File Explorer")
            os.startfile("C:\Windows\explorer.exe")
            time.sleep(3)
        elif there_exists(['powershell'],query):
            m2.speak("opening powershell")
            os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
            time.sleep(4)
        elif there_exists(['whatsapp'],query):
            m2.speak("opening whatsApp")
            os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
            time.sleep(7)
        elif there_exists(['open vlc','vlc media player','vlc player'],query):
            m2.speak("Opening VLC media player")
            os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
            time.sleep(5)

        #password generator
        elif there_exists(['suggest me a password','password suggestion please','i want a password'],query):
            m3=mini.PasswordGenerator()
            print(m3.givePSWD())

        #screeshot
        elif there_exists(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
            m2.speak("Taking screenshot")
            m2=mini.screenshot()
            m2.takeSS()
            m2.speak('Captured screenshot is saved in Screenshots folder.')

        #voice recorder
        elif there_exists(['record my voice','start voice recorder','voice recorder'],query):
            m4=mini.VoiceRecorer()
            m4.Record()
        # elif there_exists(["plus","minus","multiply","divide","power","+","-","*","/"],query):
        #     opr = query.split()[1]

        #     if opr == '+' or 'plus':
        #         m2.speak(int(query.split()[0]) + int(query.split()[2]))
        #     elif opr == '-' or 'minus':
        #         m2.speak(int(query.split()[0]) - int(query.split()[2]))
        #     elif opr == 'multiply' or 'x':
        #         m2.speak(int(query.split()[0]) * int(query.split()[2]))
        #     elif opr == 'divide' or '/':
        #         m2.speak(int(query.split()[0]) / int(query.split()[2]))
        #     elif opr == 'power' or '^':
        #         m2.speak(int(query.split()[0]) ** int(query.split()[2]))
        #     else:
        #         m2.speak("Wrong Operator")
        elif there_exists(['temperature'],query):
            try:
                res=app.query(query)
                m2.speak(next(res.results).text)
            except:
                print("Internet Connection Error")
        elif there_exists(['+','-','*','x','/','plus','add','minus','subtract','divide','multiply','divided','multiplied'],query):
            try:
                res=app.query(query)
                m2.speak(next(res.results).text)
            except:
                print("Internet Connection Error")
            
        #shutting down system
        elif there_exists(['exit','quit','shutdown','shut up','goodbye','shut down'],query):
            m2.speak("shutting down")
            sys.exit()
        
        elif there_exists(['none'],query):
            pass
        #it will give online results for the query

        elif there_exists(['search something for me','show me result for','show me results for','to do a little search','search mode'],query):
            m2.speak('What you want me to search for?')
            query=m2.takeCommand()
            m2.speak(f"Showing results for {query}")
            try:
                res=app.query(query)
                m2.speak(next(res.results).text)
            except:
                print("Sorry, but there is a little problem while fetching the result.")

        else:
            m2.speak("Sorry it did not match with any commands that i'm registered with. Please say it again.")

