import time
import webbrowser
from tkinter import *
root = Tk()
root.title("Chatbot")
cp_url = "https://dypiemr.collpoll.com/home"
maps_url= "https://www.google.com/maps"
now= time.ctime()
def send():
    send = "You -> "+e.get()
    txt.insert(END,"*" +send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi\n")
    elif(user == "hi" or user == "hii" or user == "hiii\n"):
        txt.insert(END, "\n" + "Bot -> Hello\n")
    elif(e.get() == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you\n")
    elif(e.get() == "what is your name"):
        txt.insert(END, "\n" + "Bot -> my name is Bot\n")
    elif(e.get() ==  "what is your college name"):
        txt.insert(END, "\n" + "Bot ->  DYPIEMR\n")
    elif(e.get() ==  "how old are you"):
        txt.insert(END, "\n" + "Bot -> 2 days old, LOL !\n")
    elif(user == "open collpoll"):
        webbrowser.open(cp_url)
        txt.insert(END, "\n" + "Bot ->  Opened\n")
    elif(user == "open maps"):
        webbrowser.open(maps_url)
        txt.insert(END, "\n" + "Bot ->  Opened\n")
    elif(user == "what time it is" or user=="what time it is?"):
        txt.insert(END, "\n" + "Bot ->" + now +"\n")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.\n")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I dind't got you\n")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()


"""import time
import webbrowser
cp_url = "https://dypiemr.collpoll.com/home"
maps_url= "https://www.google.com/maps"
now= time.ctime()
qna= {
    "hey":"- hello",
    "how you doing":"- I am fine",
    "what's your name":"- my name is Bot",
    "what is your college name":"- DYPIEMR",
    "open maps":"opened maps",
    "what time it is" : now,
    "open collpoll": "opened collpoll",
    "how old are you":"- 2 days old, LOL !"
   
}

while True:
    qs= input()
    if (qs=="open collpoll"):
        webbrowser.open(cp_url)
    elif(qs=="open maps"):
        webbrowser.open(maps_url)
    else:
        print("bot",qna[qs])"""
    
