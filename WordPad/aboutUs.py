from tkinter import *
from tkinter import messagebox

def AboutUs(root, TextArea):
    def abt():
        messagebox.showinfo("Team",'Team')
    F = Frame(root, bd=3, relief=GROOVE)
    F.place(x=10, y=10, width=110, height=100)

    AboutUsBtn = Button(F, text='AboutUs', font='times 12 bold', bd=3, bg='white',command=abt)
    AboutUsBtn.place(x=10, y=10, width=80, height=70)


