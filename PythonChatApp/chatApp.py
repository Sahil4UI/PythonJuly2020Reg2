import webbrowser
import os,random
from datetime import datetime as dt
chat = True
helloIntent = ['hello','hey','hey buddy','hey bro','hey wassup','hi','hie','hello dear']
byeIntent = ['bye','bie','tata','see you','see you later','will catch you later']
timeIntent = ['show me the time','tell me the time','show time','tell time','show me current time','time']
dateIntent = ['show me the date','tell me the date','show date','tell date','show me current date','date']
musicIntent = ['play music','play song']
while chat:
    msg = input("Enter Message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("hi")
    elif msg in byeIntent:
        print("tata see you later....")
        chat = False
    elif msg.startswith('open'):
        url = 'https://www.'+msg.split()[-1]+'.com'
        print(url)
        webbrowser.open(url)
    elif msg in timeIntent:
        c_time = dt.now().time()
        print(c_time.strftime('%H:%M:%S,%p'))
    elif msg in dateIntent:
        c_date = dt.now().date()
        print(c_date.strftime('%d-%m-%y,%a'))
    elif msg in musicIntent:
        os.chdir("songs")
        songsList = os.listdir()
        curr_song = random.choice(songsList)
        print(curr_song)
        os.startfile(curr_song)
    else:
        print("I don't Understand")
