from tkinter import *



def CutCopyPasteAll(root,TextArea):
    def cut():
        TextArea.event_generate("<<Cut>>")

    def copy():
        TextArea.event_generate("<<Copy>>")

    def paste():
        TextArea.event_generate("<<Paste>>")


    F=Frame(root,bd=3,relief=GROOVE)
    F.place(x=160,y=10,width=140,height=100)
    cut_button = Button(F, text="✂ Cut", font=("times new roman", 10, "bold"), bg="white",command=cut)
    cut_button.place(x=70, y=20, width=50, height=23)

    copy_button = Button(F, text="🗐 Copy", font=("times new roman", 10, "bold"), bg="white",command=copy)
    copy_button.place(x=70, y=52, width=50, height=23)

    paste_button = Button(F, text="📋 \n Paste", font=("times new roman", 12, "bold"), bg="white",command=paste)
    paste_button.place(x=10, y=20, width=50, height=55)

