
from tkinter import *




def UndoRedoAll(root,TextArea):
    def undo():
        TextArea.edit_undo()

    def redo():
        TextArea.edit_redo()

    F=Frame(root,bd=3,relief=GROOVE)
    F.place(x=310,y=10,width=110,height=100)

    undo_button = Button(F, text="↩️Undo", font=("times new roman", 10, "bold"), bg="white",command=undo)
    undo_button.place(x=10, y=20, width=80, height=23)

    redo_button = Button(F, text="↪️Redo", font=("times new roman", 10, "bold"), bg="white",command=redo)
    redo_button.place(x=10, y=52, width=80, height=23)



