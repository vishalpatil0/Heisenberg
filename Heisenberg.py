import datetime,wikipedia,webbrowser,os,random,requests,pyautogui,playsound,subprocess,time
import urllib.request,bs4 as bs,sys,threading
import Annex,wolframalpha
from ttkthemes import themed_tk
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk,Image
import sqlite3,pyjokes,pywhatkit
from functools import partial
import getpass,calendar

try:
    app=wolframalpha.Client("JPK4EE-L7KR3XWP9A")  #API key for wolframalpha
except Exception as e:
    pass

#setting chrome path
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def there_exists(terms,query):
    for term in terms:
        if term in query:
            return True

def CommandsList():
    '''show the command to which voice assistant is registered with'''
    os.startfile('Commands List.txt')

def clearScreen():
    ''' clear the scrollable text box'''
    SR.scrollable_text_clearing()

def greet():
    conn = sqlite3.connect('Heisenberg.db')
    mycursor=conn.cursor()
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        mycursor.execute('select sentences from goodmorning')
        result=mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    elif hour>=12 and hour<18:
        mycursor.execute('select sentences from goodafternoon')
        result=mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    elif hour>=18 and hour<21:
        mycursor.execute('select sentences from goodevening')
        result=mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    else:
        mycursor.execute('select sentences from night')
        result=mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    conn.commit()
    conn.close()
    SR.speak("\nMyself Heisenberg. How may I help you?")

def mainframe():
    """Logic for execution task based on query"""
    SR.scrollable_text_clearing()
    greet()
    query_for_future=None
    try:
        while(True):
            query=SR.takeCommand().lower()          #converted the command in lower case of ease of matching

            #wikipedia search
            if there_exists(['search wikipedia for','from wikipedia'],query):
                SR.speak("Searching wikipedia...")
                if 'search wikipedia for' in query:
                    query=query.replace('search wikipedia for','')
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
                elif 'from wikipedia' in query:
                    query=query.replace('from wikipedia','')
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
            elif there_exists(['wikipedia'],query):
                SR.speak("Searching wikipedia....")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)

            #jokes
            elif there_exists(['tell me joke','tell me a joke','tell me some jokes','i would like to hear some jokes',"i'd like to hear some jokes",
                            'can you please tell me some jokes','i want to hear a joke','i want to hear some jokes','please tell me some jokes',
                            'would like to hear some jokes','tell me more jokes'],query):
                SR.speak(pyjokes.get_joke(language="en", category="all"))
                query_for_future=query
            elif there_exists(['one more','one more please','tell me more','i would like to hear more of them','once more','once again','more','again'],query) and (query_for_future is not None):
                SR.speak(pyjokes.get_joke(language="en", category="all"))

            #asking for name
            elif there_exists(["what is your name","what's your name","tell me your name",'who are you'],query):
                SR.speak("My name is Heisenberg and I'm here to serve you.")
            #How are you
            elif there_exists(['how are you'],query):
                conn = sqlite3.connect('Heisenberg.db')
                mycursor=conn.cursor()
                mycursor.execute('select sentences from howareyou')
                result=mycursor.fetchall()
                temporary_data=random.choice(result)[0]
                SR.updating_ST_No_newline(temporary_data+'😃\n')
                SR.nonPrintSpeak(temporary_data)
                conn.close()
            #what is my name
            elif there_exists(['what is my name','tell me my name',"i don't remember my name"],query):
                SR.speak("Your name is "+str(getpass.getuser()))

            #calendar
            elif there_exists(['show me calendar','display calendar'],query):
                SR.updating_ST(calendar.calendar(2021))

            #google, youtube and location
            #playing on youtube
            elif there_exists(['open youtube and play','on youtube'],query):
                if 'on youtube' in query:
                    SR.speak("Opening youtube")
                    pywhatkit.playonyt(query.replace('on youtube',''))
                else:
                    SR.speak("Opening youtube")
                    pywhatkit.playonyt(query.replace('open youtube and play ',''))
                break
            elif there_exists(['play some songs on youtube','i would like to listen some music','i would like to listen some songs','play songs on youtube'],query):
                SR.speak("Opening youtube")
                pywhatkit.playonyt('play random songs')
                break
            elif there_exists(['open youtube','access youtube'],query):
                SR.speak("Opening youtube")
                webbrowser.get(chrome_path).open("https://www.youtube.com")
                break
            elif there_exists(['open google and search','google and search'],query):
                url='https://google.com/search?q='+query[query.find('for')+4:]
                webbrowser.get(chrome_path).open(url)
                break
            #image search
            elif there_exists(['show me images of','images of','display images'],query):
                url="https://www.google.com/search?tbm=isch&q="+query[query.find('of')+3:]
                webbrowser.get(chrome_path).open(url)
                break
            elif there_exists(['search for','do a little searching for','show me results for','show me result for','start searching for'],query):
                SR.speak("Searching.....")
                if 'search for' in query:
                    SR.speak(f"Showing results for {query.replace('search for','')}")
                    pywhatkit.search(query.replace('search for',''))
                elif 'do a little searching for' in query:
                    SR.speak(f"Showing results for {query.replace('do a little searching for','')}")
                    pywhatkit.search(query.replace('do a little searching for',''))
                elif 'show me results for' in query:
                    SR.speak(f"Showing results for {query.replace('show me results for','')}")
                    pywhatkit(query.replace('show me results for',''))
                elif 'start searching for' in query:
                    SR.speak(f"Showing results for {query.replace('start searching for','')}")
                    pywhatkit(query.replace('start searching for',''))
                break

            elif there_exists(['open google'],query):
                SR.speak("Opening google")
                webbrowser.get(chrome_path).open("https://www.google.com")
                break
            elif there_exists(['find location of','show location of','find location for','show location for'],query):
                if 'of' in query:
                    url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
                    webbrowser.get(chrome_path).open(url)
                    break
                elif 'for' in query:
                    url='https://google.nl/maps/place/'+query[query.find('for')+4:]+'/&amp'
                    webbrowser.get(chrome_path).open(url)
                    break
            elif there_exists(["what is my exact location","What is my location","my current location","exact current location"],query):
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)
                SR.speak("Showing your current location on google maps...")
                break
            elif there_exists(["where am i"],query):
                Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
                loc = Ip_info['region']
                SR.speak(f"You must be somewhere in {loc}")

            #who is searcing mode
            elif there_exists(['who is','who the heck is','who the hell is','who is this'],query):
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=1)
                SR.speak("According to wikipdedia:  ")
                SR.speak(results)

            #play music
            elif there_exists(['play music','play some music for me','like to listen some music'],query):
                SR.speak("Playing musics")
                music_dir='D:\\Musics\\vishal'
                songs=os.listdir(music_dir)
                # print(songs)
                indx=random.randint(0,50)
                os.startfile(os.path.join(music_dir,songs[indx]))
                break

            # top 5 news
            elif there_exists(['top 5 news','top five news','listen some news','news of today'],query):
                news=Annex.News(scrollable_text)
                news.show()

            #whatsapp message
            elif there_exists(['open whatsapp messeaging','send a whatsapp message','send whatsapp message','please send a whatsapp message'],query):
                whatsapp=Annex.WhatsApp(scrollable_text)
                whatsapp.send()
                del whatsapp
            #what is meant by
            elif there_exists(['what is meant by','what is mean by'],query):
                results=wikipedia.summary(query,sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)

            #taking photo
            elif there_exists(['take a photo','take a selfie','take my photo','take photo','take selfie','one photo please','click a photo'],query):
                takephoto=Annex.camera()
                Location=takephoto.takePhoto()
                os.startfile(Location)
                del takephoto
                SR.speak("Captured picture is stored in Camera folder.")

            #bluetooth file sharing
            elif there_exists(['send some files through bluetooth','send file through bluetooth','bluetooth sharing','bluetooth file sharing','open bluetooth'],query):
                SR.speak("Opening bluetooth...")
                os.startfile(r"C:\Windows\System32\fsquirt.exe")
                break

            #play game
            elif there_exists(['would like to play some games','play some games','would like to play some game','want to play some games','want to play game','want to play games','play games','open games','play game','open game'],query):
                SR.speak("We have 2 games right now.\n")
                SR.updating_ST_No_newline('1.')
                SR.speak("Stone Paper Scissor")
                SR.updating_ST_No_newline('2.')
                SR.speak("Snake")
                SR.speak("\nTell us your choice:")
                while(True):
                    query=SR.takeCommand().lower()
                    if ('stone' in query) or ('paper' in query):
                        SR.speak("Opening stone paper scissor...")
                        sps=Annex.StonePaperScissor()
                        sps.start(scrollable_text)
                        break
                    elif ('snake' in query):
                        SR.speak("Opening snake game...")
                        import Snake
                        Snake.start()
                        break
                    else:
                        SR.speak("It did not match the option that we have. \nPlease say it again.")

            #makig note
            elif there_exists(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
                SR.speak("What would you like to write down?")
                data=SR.takeCommand()
                n=Annex.note()
                n.Note(data)
                SR.speak("I have a made a note of that.")
                break

            #flipping coin
            elif there_exists(["toss a coin","flip a coin","toss"],query):
                moves=["head", "tails"]
                cmove=random.choice(moves)
                playsound.playsound('quarter spin flac.mp3')
                SR.speak("It's " + cmove)

            #time and date
            elif there_exists(['the time'],query):
                strTime =datetime.datetime.now().strftime("%H:%M:%S")
                SR.speak(f"Sir, the time is {strTime}")
            elif there_exists(['the date'],query):
                strDay=datetime.date.today().strftime("%B %d, %Y")
                SR.speak(f"Today is {strDay}")
            elif there_exists(['what day it is','what day is today','which day is today',"today's day name please"],query):
                SR.speak(f"Today is {datetime.datetime.now().strftime('%A')}")

            #opening software applications
            elif there_exists(['open chrome'],query):
                SR.speak("Opening chrome")
                os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
                break
            elif there_exists(['open notepad plus plus','open notepad++','open notepad ++'],query):
                SR.speak('Opening notepad++')
                os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
                break
            elif there_exists(['open notepad','start notepad'],query):
                SR.speak('Opening notepad')
                os.startfile(r'C:\Windows\notepad.exe')
                break
            elif there_exists(['open ms paint','open mspaint','open microsoft paint','start microsoft paint','start ms paint'],query):
                SR.speak("Opening Microsoft paint....")
                os.startfile('C:\Windows\System32\mspaint.exe')
                break
            elif there_exists(['show me performance of my system','open performance monitor','performance monitor','performance of my computer','performance of this computer'],query):
                os.startfile("C:\Windows\System32\perfmon.exe")
                break
            elif there_exists(['open snipping tool','snipping tool','start snipping tool'],query):
                SR.speak("Opening snipping tool....")
                os.startfile("C:\Windows\System32\SnippingTool.exe")
                break
            elif there_exists(['open code','open visual studio ','open vs code'],query):
                SR.speak("Opeining vs code")
                codepath=r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(codepath)
                break
            elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc'],query):
                SR.speak("Opening File Explorer")
                os.startfile("C:\Windows\explorer.exe")
                break
            elif there_exists(['powershell'],query):
                SR.speak("Opening powershell")
                os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
                break
            elif there_exists(['cmd','command prompt','command prom','commandpromt',],query):
                SR.speak("Opening command prompt")
                os.startfile(r'C:\Windows\System32\cmd.exe')
                break
            elif there_exists(['open whatsapp'],query):
                SR.speak("Opening whatsApp")
                os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
                break
            elif there_exists(['open settings','open control panel','open this computer setting Window','open computer setting Window'   ,'open computer settings','open setting','show me settings','open my computer settings'],query):
                SR.speak("Opening settings...")
                os.startfile('C:\Windows\System32\control.exe')
                break
            elif there_exists(['open your setting','open your settings','open settiing window','show me setting window','open voice assistant settings'],query):
                SR.speak("Opening my Setting window..")
                sett_wind=Annex.SettingWindow()
                sett_wind.settingWindow(root)
                break
            elif there_exists(['open vlc','vlc media player','vlc player'],query):
                SR.speak("Opening VLC media player")
                os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
                break

            #password generator
            elif there_exists(['suggest me a password','password suggestion','i want a password'],query):
                m3=Annex.PasswordGenerator()
                m3.givePSWD(scrollable_text)
                del m3
            #screeshot
            elif there_exists(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
                SR.speak("Taking screenshot")
                SS=Annex.screenshot()
                SS.takeSS()
                SR.speak('Captured screenshot is saved in Screenshots folder.')
                del SS

            #voice recorder
            elif there_exists(['record my voice','start voice recorder','voice recorder'],query):
                VR=Annex.VoiceRecorer()
                VR.Record(scrollable_text)
                del VR

            #text to speech conversion
            elif there_exists(['text to speech','convert my notes to voice'],query):
                SR.speak("Opening Text to Speech mode")
                TS=Annex.TextSpeech()
                del TS

            #weather report
            elif there_exists(['weather report','temperature'],query):
                Weather=Annex.Weather()
                Weather.show(scrollable_text)

            #shutting down system
            elif there_exists(['exit','quit','shutdown','shut up','goodbye','shut down'],query):
                SR.speak("shutting down")
                sys.exit()

            elif there_exists(['none'],query):
                pass
            elif there_exists(['stop the flow','stop the execution','halt','halt the process','stop the process','stop listening','stop the listening'],query):
                SR.speak("Listening halted.")
                break
            #it will give online results for the query
            elif there_exists(['search something for me','to do a little search','search mode','i want to search something'],query):
                SR.speak('What you want me to search for?')
                query=SR.takeCommand()
                SR.speak(f"Showing results for {query}")
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Sorry, but there is a little problem while fetching the result.")

            #what is the capital
            elif there_exists(['what is the capital of','capital of','capital city of'],query):
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Sorry, but there is a little problem while fetching the result.")

            elif there_exists(['temperature'],query):
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Internet Connection Error")
            elif there_exists(['+','-','*','x','/','plus','add','minus','subtract','divide','multiply','divided','multiplied'],query):
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Internet Connection Error")

            else:
                SR.speak("Sorry it did not match with any commands that i'm registered with. Please say it again.")
    except Exception as e:
        pass

def gen(n):
    for i in range(n):
        yield i

class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        mainframe()

def Launching_thread():
    Thread_ID=gen(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()

if __name__=="__main__":
        #tkinter code
        root=themed_tk.ThemedTk()
        root.set_theme("winnative")
        root.geometry("{}x{}+{}+{}".format(745,360,int(root.winfo_screenwidth()/2 - 745/2),int(root.winfo_screenheight()/2 - 360/2)))
        root.resizable(0,0)
        root.title("Heisenberg")
        root.iconbitmap('Heisenberg.ico')
        root.configure(bg='#2c4557')
        scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=15,width=87,relief='sunken',bd=5,wrap=tk.WORD,bg='#add8e6',fg='#800000')
        scrollable_text.place(x=10,y=10)
        mic_img=Image.open("Mic.png")
        mic_img=mic_img.resize((55,55),Image.ANTIALIAS)
        mic_img=ImageTk.PhotoImage(mic_img)
        Speak_label=tk.Label(root,text="SPEAK:",fg="#FFD700",font='"Times New Roman" 12 ',borderwidth=0,bg='#2c4557')
        Speak_label.place(x=250,y=300)
        """Setting up objects"""
        SR=Annex.SpeakRecog(scrollable_text)    #Speak and Recognition class instance
        Listen_Button=tk.Button(root,image=mic_img,borderwidth=0,activebackground='#2c4557',bg='#2c4557',command=Launching_thread)
        Listen_Button.place(x=330,y=280)
        myMenu=tk.Menu(root)
        m1=tk.Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared of from the window
        m1.add_command(label='Commands List',command=CommandsList)
        myMenu.add_cascade(label="Help",menu=m1)
        stng_win=Annex.SettingWindow()
        myMenu.add_cascade(label="Settings",command=partial(stng_win.settingWindow,root))
        myMenu.add_cascade(label="Clear Screen",command=clearScreen)
        root.config(menu=myMenu)
        root.mainloop()