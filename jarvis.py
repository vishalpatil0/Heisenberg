import datetime,wikipedia,webbrowser,os,random,requests,pyautogui,playsound,subprocess,time
import urllib.request,bs4 as bs,sys
import mini,wolframalpha
import StonePaperScissor as SPS
from ttkthemes import themed_tk
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext

"""Setting up objects"""
SR=mini.SpeakRecog()    #Speak and Recognition class instance

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
    if hour<=4 and hour<12:
        SR.speak("Good Morning!")
    elif hour>=12 and hour<18:
        SR.speak("Good Afternoon!")
    elif hour>=18 and hour<21:
        SR.speak("Good Evening!")
    else:
        SR.speak("It is a beautiful night.")
    SR.speak("I am jarvis sir. How may I help you.")

def mainframe():
    SR.scrollable_text_clearing()
    # greet()
    """Logic for execution task based on query"""
    try:
        while(True):
            query=SR.takeCommand().lower()

            #wikipedia search
            if there_exists(['wikipedia'],query):
                SR.speak("Searching wikipedia....")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)

            elif there_exists(["what is your name","what's your name","tell me your name"],query):
                SR.speak("My name is Jarvis and i'm here to serve you.")

            #google, youtube and location
            elif there_exists(['open youtube','access youtube'],query):
                SR.speak("Opening youtube")
                webbrowser.get(chrome_path).open("https://www.youtube.com")
                break
            elif there_exists(['open google and search','google and search'],query):
                url='https://google.com/search?q='+query[query.find('for')+4:]
                webbrowser.get(chrome_path).open(url)
                break
            elif there_exists(['open google'],query):
                SR.speak("Opening google")
                webbrowser.get(chrome_path).open("https://www.google.com")
                break
            elif there_exists(['find location of'],query):
                url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
                webbrowser.get(chrome_path).open(url)
                break
            elif there_exists(["what is my exact location","What is my location","my current location"],query):
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)
                SR.speak("Showing your current location on google maps...")
                break
            elif there_exists(["where am i"],query):
                Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
                loc = Ip_info['region']
                SR.speak(f"You must be somewhere in {loc}")

            #play music
            elif there_exists(['play music'],query):
                SR.speak("Playing musics")
                music_dir='D:\\Musics\\vishal'
                songs=os.listdir(music_dir)
                # print(songs)
                indx=random.randint(0,50)
                os.startfile(os.path.join(music_dir,songs[indx]))
                break

            #play game
            elif there_exists(['would like to play some games','play some games','would like to play some game','want to play some games','want to play game','want to play games','play games','open games','play game','open game'],query):
                SR.speak("We have 3 games right now.")
                print('1. ',end='')
                SR.speak("Stone Paper Scissor")
                print('2. ',end='')
                SR.speak("Guess the number")
                print('3. ',end='')
                SR.speak("Snake")
                SR.speak("Tell us your choice")
                while(True):
                    query=SR.takeCommand().lower()
                    if ('stone' in query) or ('paper' in query):
                        SR.speak("Opening stone paper scissor...")
                        SPS.start()
                        break
                    elif ('guess' in query) or ('number' in query):
                        SR.speak("Opening Guess the number...")
                        m7=mini.GuessTheNumber()
                        m7.start(scrollable_text)
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
                n=mini.note()
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
            elif there_exists(['whatsapp'],query):
                SR.speak("Opening whatsApp")
                os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
                break
            elif there_exists(['open vlc','vlc media player','vlc player'],query):
                SR.speak("Opening VLC media player")
                os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
                break

            #password generator
            elif there_exists(['suggest me a password','password suggestion','i want a password'],query):
                m3=mini.PasswordGenerator()
                m3.givePSWD(scrollable_text)
                del m3
            #screeshot
            elif there_exists(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
                SR.speak("Taking screenshot")
                SS=mini.screenshot()
                SS.takeSS()
                SR.speak('Captured screenshot is saved in Screenshots folder.')
                del SS

            #voice recorder
            elif there_exists(['record my voice','start voice recorder','voice recorder'],query):
                VR=mini.VoiceRecorer()
                VR.Record(scrollable_text)
                del VR

            #text to speech conversion
            elif there_exists(['text to speech','convert my notes to voice'],query):
                SR.speak("Opening Text to Speech mode")
                TS=mini.TextSpeech()
                del TS
            # elif there_exists(["plus","minus","multiply","divide","power","+","-","*","/"],query):
            #     opr = query.split()[1]

            #     if opr == '+' or 'plus':
            #         SR.speak(int(query.split()[0]) + int(query.split()[2]))
            #     elif opr == '-' or 'minus':
            #         SR.speak(int(query.split()[0]) - int(query.split()[2]))
            #     elif opr == 'multiply' or 'x':
            #         SR.speak(int(query.split()[0]) * int(query.split()[2]))
            #     elif opr == 'divide' or '/':
            #         SR.speak(int(query.split()[0]) / int(query.split()[2]))
            #     elif opr == 'power' or '^':
            #         SR.speak(int(query.split()[0]) ** int(query.split()[2]))
            #     else:
            #         SR.speak("Wrong Operator")
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

            #shutting down system
            elif there_exists(['exit','quit','shutdown','shut up','goodbye','shut down'],query):
                SR.speak("shutting down")
                sys.exit()

            elif there_exists(['none'],query):
                pass
            #it will give online results for the query

            elif there_exists(['search something for me','show me result for','show me results for','to do a little search','search mode'],query):
                SR.speak('What you want me to search for?')
                query=SR.takeCommand()
                SR.speak(f"Showing results for {query}")
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Sorry, but there is a little problem while fetching the result.")

            else:
                SR.speak("Sorry it did not match with any commands that i'm registered with. Please say it again.")
    except Exception as e:
        pass

if __name__=="__main__":
        #tkinter code
        root=themed_tk.ThemedTk()
        # root.set_theme("winnative")
        root.geometry('900x400+230+80')
        root.resizable(0,0)
        scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=15,width=85,relief='sunken',bd=5)
        scrollable_text.place(x=90,y=10)
        Listen_Button=tk.Button(root,text="Listen",command=mainframe)
        Listen_Button.place(x=400,y=280)
        SR.STS(scrollable_text)
        root.mainloop()