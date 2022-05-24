from tkinter import *


def newFile():
    pass
def openFile():
    pass
def saveFile():
    pass

def about():
    pass
def SaveOpenNew(root):

    F=Frame(root,bd=3,relief=GROOVE)
    F.place(x=10,y=10,width=140,height=100)

    Save_button = Button(F, text="Save", font=("times new roman", 10, "bold"), bg="white",command=saveFile)
    Save_button.place(x=10, y=20, width=50, height=55)

    new_button = Button(F, text="New", font=("times new roman", 10, "bold"), bg="white",command=newFile)
    new_button.place(x=70, y=20, width=50, height=23)
    open_button = Button(F, text="Open", font=("times new roman", 10, "bold"), bg="white",command=openFile)
    open_button.place(x=70, y=52, width=50, height=23)
