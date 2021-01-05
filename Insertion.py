import sqlite3,random
            
conn = sqlite3.connect('Heisenberg.db')
mycursor=conn.cursor()

list1=['Good to hear from you! How may I help',
        "I'm fine, thank you. What can I do for you?",
        "Very Good, How may I help you",
        "Wonderful thanks, What can I do for you?",
        "I'm well, thank you, how can I help",
        "So glad to hear your voice, How can I help you?",
        "I'm doing great, thanks for asking. Anything I can help with"]

for i in list1:       
    mycursor.execute('insert into howareyou(sentences) values (?)',(i,))

conn.commit()
conn.close()