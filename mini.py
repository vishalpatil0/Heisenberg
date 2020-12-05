import datetime,subprocess,os,pyautogui,string,random
import pyttsx3
import speech_recognition as sr
import sounddevice
from scipy.io.wavfile import write
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import pyperclip
from ttkthemes import themed_tk as tkth
import tkinter.scrolledtext as scrolledtext
from functools import partial

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
    scrollable_text=None
    def STS(self,scrollable_text):
        '''This is scrollable text sette '''
        self.scrollable_text=scrollable_text
    def updating_ST(self,data):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data+'\n')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()
    def scrollable_text_clearing(self):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.delete(1.0,'end')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.update()
    def speak(self,audio):
        """It speaks the audio"""
        self.updating_ST(audio)
        self.engine.say(audio)
        # engine.save_to_file('Hello World', 'test.mp3')
        self.engine.runAndWait()
        # engine.stop()

    def nonPrintSpeak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        """It take microphone input from the user and return string"""
        recog=sr.Recognizer()
        # mic=Microphone()
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            self.updating_ST("Listening...")
            recog.pause_threshold = 1
            # r.energy_threshold = 45.131829621150224
            # print(sr.Microphone.list_microphone_names())
            #print(r.energy_threshold)
            audio=recog.listen(source)
        try:
            self.updating_ST("Recognizing...")
            query= recog.recognize_google(audio)
            self.updating_ST(f"You: {query}\n")
        except Exception as e:
            # print(e)
            self.updating_ST("Say that again please...")
            return 'None'
        return query

class PasswordGenerator:
    def action(self,pswd):
        pyperclip.copy(pswd)
    def showpswd(self,data,pswd):
        root=tk.Toplevel()
        style = ttk.Style()
        style.configure('W.TButton',font=('calibri', 10, 'bold'),foreground ='purple',borderwidth ='4',background="pink")
        root.geometry("320x80+540+270")
        # root.eval('tk::PlaceWindow . center')     #this only works for Tk() instance not for Toplevel() instance
        label1=ttk.Label(root,text=data,font=("comicsansms",9,'bold')).pack()
        button1=ttk.Button(root,text='Copy to clipboard',style = 'W.TButton',command=partial(self.action,pswd)).pack(pady=20)
        root.resizable(0,0)
        root.mainloop()
        del root
    def givePSWD(self,scrollable_text):
        SR=SpeakRecog()
        SR.STS(scrollable_text)
        SR.speak("What type of password you want?")
        SR.updating_ST("\nPassword Level we have:-\n\nPoor Level\nAverage Level\nStrong Level\n")
        while(True):
            query=SR.takeCommand().lower()
            if ('poor' in query):
                self.showpswd("Your Password is : "+"".join(random.sample(string.ascii_letters,7)),"".join(random.sample(string.ascii_letters,7)))
                break
            elif ('average' in query):
                self.showpswd("Your Password is : "+"".join(random.sample(string.ascii_letters+string.digits,10)),"".join(random.sample(string.ascii_letters+string.digits,10)))
                break
            elif ('strong' in query):
                self.showpswd("Your Password is : "+"".join(random.sample(string.ascii_letters+string.digits+string.punctuation,13)),"".join(random.sample(string.ascii_letters+string.digits+string.punctuation,13)))
                break
            else:
                SR.speak("Please say it again")
        del SR
        
class TextSpeech:
    def txtspk(self):
        SR=SpeakRecog()
        SR.nonPrintSpeak(self.text.get(1.0,tk.END))
        del SR
    def opentxt(self):
        self.root.focus_force()    
        try:
            file_path=filedialog.askopenfilename(initialdir =r"C:\Users\Vishal\Documents\Projects or important programs\jarvis\Notes",title="Select file",filetypes=(('text file',"*.txt"),("All files", "*.*")))
            with open(file_path,'r') as f:
                g=f.read()
        
            self.root.focus_force()    
            self.text.delete(1.0,tk.END)
            self.text.insert(tk.INSERT,g)
            self.text.update()
            SR=SpeakRecog()
            SR.nonPrintSpeak(g)
            del SR
        except FileNotFoundError as e:
            self.root.focus_force()    
            pass

    def __init__(self):
        self.root=tkth.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("radiance")
        self.root.resizable(0,0)
        self.root.configure(background='white')
        self.root.title("Text to Speech")
        #root widget
        self.text=scrolledtext.ScrolledText(self.root,width=30,height=10,wrap=tk.WORD,padx=10,pady=10,borderwidth=5,relief=tk.RIDGE)
        self.text.grid(row=0,columnspan=3)
        #buttons
        self.listen_btn=ttk.Button(self.root,text="Listen",width=7,command=self.txtspk).grid(row=2,column=0,ipadx=2)
        self.clear_btn=ttk.Button(self.root,text="Clear",width=7,command=lambda:self.text.delete(1.0,tk.END)).grid(row=2,column=1,ipadx=2)
        self.open_btn=ttk.Button(self.root,text="Open",width=7,command=self.opentxt).grid(row=2,column=2,ipadx=2)
        self.root.focus_set()
        self.root.mainloop()
    
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

class GuessTheNumber:
    def start(self,scrollable_text):
        n=random.randint(1,10)
        SR=SpeakRecog()
        SR.STS(scrollable_text)
        attempt=0
        SR.speak("Guess a number between 1 to 10. \nTo become winner of the game you need to guess the number within 3 attempts.")
        while(True):
            guess=int(input("Enter number: "))
            if guess<n:
                SR.speak("Your guess was low.")
            elif guess>n:
                SR.speak("Your guess was high")
            elif guess==n:
                SR.speak("yep you got it.")
                break
            else:
                SR.speak("Invalid data. Please enter right data.")
            attempt+=1
        if attempt>=3:
            print(f"Your attempts= {attempt}")
            SR.speak("Looser. \n Good luck next time")
        else:
            SR.speak("Congratulations. You are winner of the game.")
        del SR

class VoiceRecorer:
    def Record(self,scrollable_text):
        SR=SpeakRecog()
        SR.STS(scrollable_text)
        SR.speak("This recording is of 10 seconds.")
        fs=44100
        second=10
        SR.updating_ST("Recording.....")
        record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
        sounddevice.wait()
        a=os.getcwd()
        if not os.path.exists("Recordings"):
            os.mkdir("Recordings")
        os.chdir(a+'\Recordings')
        write("Recording-"+str(datetime.datetime.now()).replace(':','-')+".wav",fs,record_voice)
        SR.speak("Voice is recorded in \'Recordings\' folder.")
        os.chdir(a)
        del SR