from tkinter import *
from tkinter import ttk
from tkinter import font


def FontPanel(root, TextArea):
    def Italic():
        # italic_font = font.Font(TextArea, TextArea.cget("font"))
        # italic_font.configure(slant='italic')
        TextArea.tag_configure("italic", font=TextArea.cget("font") + " italic")
        try:
            current_tags = TextArea.tag_names('sel.first')

            if 'italic' in current_tags:
                TextArea.tag_remove("italic", 'sel.first', 'sel.last')
            else:
                TextArea.tag_add("italic", 'sel.first', 'sel.last')
        except:
            pass

    def Bold():
        TextArea.tag_configure("bold", font=TextArea.cget("font") + " bold")
        try:
            current_tags = TextArea.tag_names('sel.first')

            if 'bold' in current_tags:
                TextArea.tag_remove("bold", 'sel.first', 'sel.last')
            else:
                TextArea.tag_add("bold", 'sel.first', 'sel.last')
        except:
            pass

    def UnderLine():

        Underline_font = font.Font(TextArea, TextArea.cget("font"))
        Underline_font.configure(underline=True)
        TextArea.tag_configure("underline", font=Underline_font)

        try:
            current_tags = TextArea.tag_names('sel.first')

            if 'underline' in current_tags:
                TextArea.tag_remove("underline", 'sel.first', 'sel.last')
            else:
                TextArea.tag_add("underline", 'sel.first', 'sel.last')
        except:
            pass

    def background():
        TextArea.tag_configure("bg", background="yellow", foreground="black")
        current_tags = TextArea.tag_names('sel.first')
        if 'bg' in current_tags:
            TextArea.tag_remove("bg", "1.0", 'end')
        else:
            TextArea.tag_add("bg", "sel.first", "sel.last")

    def center():
        TextArea.tag_configure("right", justify=RIGHT)
        TextArea.tag_configure("center", justify='center')
        TextArea.tag_configure("left", justify=LEFT)

        current_tags = TextArea.tag_names('sel.first')
        if 'center' in current_tags:
            TextArea.tag_remove("center", "1.0", 'end')
            TextArea.tag_remove("right", "1.0", 'end')
            TextArea.tag_remove("left", "1.0", 'end')
        else:
            TextArea.tag_remove("center", "1.0", 'end')
            TextArea.tag_remove("right", "1.0", 'end')
            TextArea.tag_remove("left", "1.0", 'end')
            TextArea.tag_add("center", "1.0", "end")

    def right():
        TextArea.tag_configure("right", justify=RIGHT)
        current_tags = TextArea.tag_names('sel.first')

        if 'right' in current_tags:
            TextArea.tag_remove("center", "1.0", 'end')
            TextArea.tag_remove("right", "1.0", 'end')
            TextArea.tag_remove("left", "1.0", 'end')
        else:
            TextArea.tag_remove("center", "1.0", 'end')
            TextArea.tag_remove("right", "1.0", 'end')
            TextArea.tag_remove("left", "1.0", 'end')
            TextArea.tag_add("right", "1.0", "end")

    def left():
        TextArea.tag_configure("left", justify=LEFT)
        current_tags = TextArea.tag_names('sel.first')

        if 'left' in current_tags:
            TextArea.tag_remove("center", "1.0", 'end')
            TextArea.tag_remove("right", "1.0", 'end')
            TextArea.tag_remove("left", "1.0", 'end')
        else:
            TextArea.tag_remove("center", "1.0", 'end')
            TextArea.tag_remove("right", "1.0", 'end')
            TextArea.tag_remove("left", "1.0", 'end')
            TextArea.tag_add("left", "1.0", "end")

    TF = Frame(root, bd=3, relief=GROOVE)
    TF.place(x=430, y=10, width=800, height=100)

    FontList = ['Calibri', 'Arial', 'Algerian', 'Agency FB']
    FontSize = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
    FontFG = ['black', 'red', 'blue', 'yellow', 'orange', 'violet', 'white']


    fontStyleVariable = StringVar()
    fontSizeVariable = StringVar()

    FontListLbl = ttk.Combobox(TF, value=FontList, font=('times new roman', 15, 'bold'))
    FontListLbl.place(x=10, y=10, width=200, height=30)
    FontListLbl.current(0)

    FontSizeLbl = ttk.Combobox(TF, value=FontSize, font=('times new roman', 15, 'bold'))
    FontSizeLbl.place(x=220, y=10, width=50, height=30)
    FontSizeLbl.current(7)

    BoldBtn = Button(TF, bd=2, relief=GROOVE, text="B", font='times 15 bold', bg='white', command=Bold)
    BoldBtn.place(x=10, y=55, width=30, height=30)

    ItalicBtn = Button(TF, bd=2, relief=GROOVE, text="I", font='times 15 italic', bg='white', command=Italic)
    ItalicBtn.place(x=45, y=55, width=30, height=30)

    UnderLineBtn = Button(TF, bd=2, relief=GROOVE, text="U", font='times 15 underline', bg='white', command=UnderLine)
    UnderLineBtn.place(x=80, y=55, width=30, height=30)

    FontpBtn = Button(TF, bd=2, relief=GROOVE, text="A+", font=('times new roman', 15, 'bold'), bg='white')
    FontpBtn.place(x=280, y=10, width=30, height=30)

    FontmBtn = Button(TF, bd=2, relief=GROOVE, text="A-", font=('times new roman', 15, 'bold'), bg='white')
    FontmBtn.place(x=315, y=10, width=30, height=30)



    fg = Button(TF, text="fg", bg='white', relief=GROOVE, bd=2, font=('times new roman', 15, 'bold'), )
    fg.place(x=130, y=55, width=30, height=30)


    FontBG = ['bg', 'black', 'red', 'blue', 'yellow', 'orange', 'violet', 'white']
    def selected(event):
        mar = BG.get().lower()

        if mar == 'FG':
            pass
        else:
            TextArea.tag_configure("bg", background=mar)
            current_tags = TextArea.tag_names('sel.first')
            if 'bg' in current_tags:
                #TextArea.tag_remove("bg", "1.0", 'end')
                TextArea.tag_remove("bg", "sel.first", 'sel.last')
            else:
                TextArea.tag_add("bg", "sel.first", "sel.last")

            BG.set(FontBG[0])

    BG = StringVar()
    BG.set(FontBG[0])


    bg = OptionMenu(TF, BG, *FontBG, command=selected)
    bg.place(x=165, y=55, width=30, height=30)

    Left = Button(TF, text="-  ", bg='white', relief=GROOVE, bd=2, font=('times new roman', 15, 'bold'), command=left)
    Left.place(x=215, y=55, width=30, height=30)

    Center = Button(TF, text=" - ", bg='white', relief=GROOVE, bd=2, font=('times new roman', 15, 'bold'),
                    command=center)
    Center.place(x=250, y=55, width=30, height=30)

    Right = Button(TF, text="  -", bg='white', relief=GROOVE, bd=2, font=('times new roman', 15, 'bold'), command=right)
    Right.place(x=285, y=55, width=30, height=30)

    def FP():
        a=Label(root)
        FLL=FontListLbl.get()
        FSL=FontSizeLbl.get()


        """try:
            TextArea.tag_add(fontStyleVariable.get(), "sel.first", "sel.last")
            TextArea.tag_config(fontStyleVariable.get(), font=(fontStyleVariable.get(), False))
        except:
            pass

        try:

            TextArea.tag_add(fontSizeVariable.get(), "sel.first", "sel.last")
            TextArea.tag_config(fontSizeVariable.get(), font=(False, fontSizeVariable.get()))
        except:
            pass"""

        TextArea.config(font=(f'{FLL}',FSL))
        a.after(100,FP)

    FP()



