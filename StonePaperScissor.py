import random
from mini import SpeakRecog

SR=SpeakRecog()

def start():
    list1=['stone','paper','scissor']
    while(True):
        print("\n\n--------------------------------welcome-----------------------------")
        SR.speak("\n\nThis game is contain 3 rounds, those who win maximum rounds is the winner of this game.")
        human_score=0
        computer_score=0
        i=0
        while(i<3):
            if i==2:
                if(human_score>computer_score):
                    SR.speak("\nNo need of 3rd round because human's score is obviously greater thean computer's.\n")
                    break
                elif(human_score<computer_score):
                    SR.speak("\nNo need of 3rd round because computer's score is obviously greater thean human's.\n")
                    break

            print(50*"*")
            while(True):
                SR.speak("Your choice please-")
                user_ip=SR.takeCommand().lower()
                if(('stone' in user_ip) or ('paper' in user_ip) or ('scissor' in user_ip) or ('cutter' in user_ip) or ('rock' in user_ip)):
                    if(user_ip=='cutter'):
                        user_ip='scissor'
                    if(user_ip=='rock'):
                        user_ip='stone'
                    break
                else:
                    SR.speak("\nIt did not match with the option that we have. Please enter your choice again.")
            comp_ip=random.choice(list1)
            if(user_ip==comp_ip):
                SR.speak("\nIt is a tie, so it is not considered as a round.\n")

            elif((user_ip=='stone' and comp_ip=='paper') or (user_ip=='paper' and comp_ip=='scissor') or (user_ip=='scissor' and comp_ip=='stone') ):
                computer_score+=1
                SR.speak("\nComputer win this round\n")
                SR.speak(f"\nComputre's choice was {comp_ip}\n")
                print(50*"+")
                i+=1
            elif((comp_ip=='stone' and user_ip=='paper') or (user_ip=='scissor' and comp_ip=='paper') or (user_ip=='stone' and comp_ip=='scissor')):
                human_score+=1
                SR.speak("\nHuman win this round\n")
                SR.speak(f"\nComputre's choice was {comp_ip}\n")
                print(50*"+")
                i+=1
        
            
            
        if(human_score==computer_score):
            SR.speak("\nIt is a tie\n")
        elif(human_score>computer_score):
            SR.speak("\nHuman is the winner of this game \n")    
        else:
            SR.speak("\nComputer is the winner of this game\n")
        print(50*"*")
        SR.speak('If you want repeat this game then say REPEAT.')
        decision=SR.takeCommand().lower()
        if(decision=='repeat'):
            pass
        else:
            SR.speak("Getting out of this game to main thread.")
            break

