import random
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    """It speaks the audio"""
    print(audio)
    engine.say(audio)
    # engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
    # engine.stop()

def takeCommand():
    recog=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recog.pause_threshold = 1
        audio=recog.listen(source)
    try: 
        print("Recognizing...")
        query= recog.recognize_google(audio)
        speak(f"User said: {query}\n")
    except Exception as e:
        return 'None'
    return query

def start():
    list1=['stone','paper','scissor']
    while(True):
        print("\n\n--------------------------------welcome-----------------------------")
        speak("\n\nThis game is of 3 round those who win  2 round is the winner of the game")
        human_score=0
        computer_score=0
        i=0
        while(i<3):
            if i==2:
                if(human_score>computer_score):
                    speak("\nNo need of 3rd round bcoz human's score is obviously greater thean computer's.\n")
                    break
                elif(human_score<computer_score):
                    speak("\nNo need of 3rd round bcoz computer's score is obviously greater thean human's.\n")
                    break

            print(50*"*")
            while(True):
                speak("Your choice please-")
                user_ip=takeCommand().lower()
                if(user_ip=='stone' or user_ip=='paper' or user_ip=='scissor' or user_ip=='cutter' or user_ip=='rock'):
                    if(user_ip=='cutter'):
                        user_ip='scissor'
                    if(user_ip=='rock'):
                        user_ip='stone'
                    break
                else:
                    speak("\nIt did not match with the option that we have. Please enter your choice again.")
            comp_ip=random.choice(list1)
            if(user_ip==comp_ip):
                speak("\nIt is a tie, so it is not considered as a round.\n")

            elif((user_ip=='stone' and comp_ip=='paper') or (user_ip=='paper' and comp_ip=='scissor') or (user_ip=='scissor' and comp_ip=='stone') ):
                computer_score+=1
                speak("\nComputer win this round\n")
                speak(f"\nComputre choice was {comp_ip}\n")
                print(50*"+")
                i+=1
            elif((comp_ip=='stone' and user_ip=='paper') or (user_ip=='scissor' and comp_ip=='paper') or (user_ip=='stone' and comp_ip=='scissor')):
                human_score+=1
                speak("\nHuman win this round\n")
                speak(f"\nComputre choice was {comp_ip}\n")
                print(50*"+")
                i+=1
        
            
            
        if(human_score==computer_score):
            speak("\nIt is a tie\n")
        elif(human_score>computer_score):
            speak("\nHuman is the winner of this game \n")    
        else:
            speak("\nComputer is the winner of this game\n")
        print(50*"*")
        speak('If you want repeat this game then say REPEAT.')
        decision=takeCommand().lower()
        if(decision!='repeat'):
            break
