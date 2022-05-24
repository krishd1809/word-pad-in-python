from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import font
import pyttsx3
import re
def Speak(root,TextArea):
    engine = pyttsx3.init()
    def talk():

        engine.say(TextArea.get(1.0,END))
        engine.runAndWait()
    def stop():
        engine.stop()

    F = Frame(root, bd=3, relief=GROOVE)
    F.place(x=10, y=10, width=100, height=100)

    Speaklabel = Button(F, text="Read Aloud", font=("times new roman", 10, "bold"), bg="white", relief=GROOVE, command=talk)
    Speaklabel.place(x=10, y=15, width=75, height=23)

    my_button = Button(F, text="Stop", font=("times new roman", 10, "bold"), bg="white", relief=GROOVE, command=stop)
    my_button.place(x=10, y=55, width=75, height=23)




def wordCount(root, TextArea):
    def WC():
        word = TextArea.get(0.0, END)
        wordcount = len(re.findall('\w+', word))


        c=0
        C=-1
        for k in word:
            if k==' ' or k=='\n':
                C=C+1
            else:
                c=c+1
                C=C+1
        charSpace = C
        charNoSpace=c
        c=0
        for k in word:
            if k=='\n':
                c=c+1
        lines=c

        messagebox.showinfo('Char Count',f"Words: {wordcount}\nCharacter(With Space): {charSpace}\nCharacter(Without "
                                         f"Space): {charNoSpace}\nLines: {lines}")
    F = Frame(root, bd=3, relief=GROOVE)
    F.place(x=120, y=10, width=100, height=100)

    Speaklabel = Button(F, text="Word\nCount", font=("times new roman", 10, "bold"), bg="white", relief=GROOVE,
                        command=WC)
    Speaklabel.place(x=10, y=15, width=75, height=65)














