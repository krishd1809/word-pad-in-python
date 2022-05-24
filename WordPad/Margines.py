from tkinter import *
from tkinter import ttk


def Margines(root,TextArea):
    Mar = ['Default',
           '10,10px',
           '20,20px',
           '30,30px',
           '40,40px',
           '50,50px']

    def selected(event):
        mar = clicked.get()

        if mar == 'Default':
            TextArea.config(padx=0, pady=0)
        elif mar == '10,10px':
            TextArea.config(padx=10, pady=10)
        elif mar == '20,20px':
            TextArea.config(padx=20, pady=20)
        elif mar == '30,30px':
            TextArea.config(padx=30, pady=30)
        elif mar == '40,40px':
            TextArea.config(padx=40, pady=40)

        elif mar == '50,50px':
            TextArea.config(padx=50, pady=50)


    clicked = StringVar()
    clicked.set(Mar[0])

    F = Frame(root, bd=3, relief=GROOVE)
    F.place(x=10, y=10, width=100, height=100)

    marginelabel = Label(F, text="Margins", font=("times new roman", 10, "bold"), bg="white", relief=GROOVE)
    marginelabel.place(x=10, y=15, width=75, height=23)

    margin_Box = OptionMenu(F, clicked, *Mar, command=selected)
    margin_Box.place(x=5, y=55)







