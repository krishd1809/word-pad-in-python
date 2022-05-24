from tkinter import *
from tkinter.filedialog import askopenfilename


def ImageF(root,TextArea):
    F = Frame(root, bd=3, relief=GROOVE)
    F.place(x=1300, y=10, width=100, height=100)

    def Img():
        my_image = PhotoImage(file="a.png")
        TextArea.image_create(END, image=my_image)
        position = TextArea.index(INSERT)
        TextArea.config(text=position)


    img_button = Button(F, text="🖼",font=("times new roman", 30), bg="white",command=Img)
    img_button.place(x=20, y=20, width=50, height=50)


