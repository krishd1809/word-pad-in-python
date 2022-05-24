import re
from tkinter import *
from tkinter import ttk
from CutCopyPaste import *
from Image import *
from NewSaveOpen import *
from UndoRedo import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from FontPanel import *
from Margines import *
from helpSupport import *
from aboutUs import *
from Review import *


class Writepad:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1522x770+0+0')
        self.root.title('WritePad')

        self.TextFrame = Frame(self.root, bd=5, relief=RIDGE)
        self.TextFrame.place(x=20, y=150, width=1482, height=580)

        canvas = Canvas(self.TextFrame, bg='black')
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        vert_scroll = ttk.Scrollbar(self.TextFrame, orient=VERTICAL, command=canvas.yview)
        vert_scroll.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=vert_scroll.set, )
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        sec_frame = Frame(canvas)
        sec_frame.pack(fill=BOTH, expand=1)
        canvas.create_window((0, 0), window=sec_frame, anchor="nw")

        self.TextArea = Text(sec_frame, undo=True)
        self.TextArea.pack(side=RIGHT, fill=BOTH, expand=1)

        #self.TextArea.configure(yscrollcommand=vert_scroll.set, )
        #self.TextArea.bind('<Configure>', lambda e: self.TextArea.configure(scrollregion=self.TextArea.bbox("all")))



        MenuBar = Menu(self.root)

        FileMenu = Menu(MenuBar, tearoff=0)
        FileMenu.add_command(label="New", command=self.newFile)
        FileMenu.add_command(label="Open", command=self.openFile)
        FileMenu.add_command(label="Save", command=self.saveFile)
        FileMenu.add_separator()

        FileMenu.add_command(label="Exit", command=self.quitApp)
        MenuBar.add_cascade(label="File", menu=FileMenu)

        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About", command=about)
        MenuBar.add_cascade(label="Edit", menu=HelpMenu)

        root.config(menu=MenuBar)

        """Scroll = Scrollbar(self.TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=Scroll.set)"""

        s = ttk.Style()
        s.configure('TNotebook.Tab', font=('times', '12', 'bold'), borderwidth=2, width=15)

        tabControl = ttk.Notebook(self.root)
        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tab3 = Frame(tabControl)
        tab4 = Frame(tabControl)
        tab5 = Frame(tabControl)

        tabControl.add(tab1, text='Home')
        tabControl.add(tab2, text='Design&Layout')
        tabControl.add(tab5, text='Review')
        tabControl.add(tab3, text='Help&Support')
        tabControl.add(tab4, text='About Us')
        tabControl.place(x=0, y=0, width=1522, height=150)

        CutCopyPasteAll(tab1, self.TextArea)
        ImageF(tab1, self.TextArea)
        self.SaveOpenNew(tab1)
        UndoRedoAll(tab1, self.TextArea)
        FontPanel(tab1, self.TextArea)
        Margines(tab2, self.TextArea)
        HelpSupport(self.root,tab3, self.TextArea)
        AboutUs(tab4, self.TextArea)
        Speak(tab5, self.TextArea)
        wordCount(tab5, self.TextArea)

        self.DownBar()
    def SaveOpenNew(self, tab1):

        F = Frame(tab1, bd=3, relief=GROOVE)
        F.place(x=10, y=10, width=140, height=100)

        Save_button = Button(F, text="Save", font=("times new roman", 10, "bold"), bg="white", command=self.saveFile)
        Save_button.place(x=10, y=20, width=50, height=55)

        new_button = Button(F, text="New", font=("times new roman", 10, "bold"), bg="white", command=self.newFile)
        new_button.place(x=70, y=20, width=50, height=23)
        open_button = Button(F, text="Open", font=("times new roman", 10, "bold"), bg="white", command=self.openFile)
        open_button.place(x=70, y=52, width=50, height=23)

    def newFile(self):
        self.root.title("WritePad")
        self.file = None
        self.TextArea.delete(1.0, END)


        """Scroll = Scrollbar(self.TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=Scroll.set)"""

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file) + " WritePad")
            self.TextArea.delete(1.0, END)

            """Scroll = Scrollbar(self.TextArea)
            Scroll.pack(side=RIGHT, fill=Y)
            Scroll.config(command=self.TextArea.yview)
            self.TextArea.config(yscrollcommand=Scroll.set)"""
            f = open(self.file, 'r')
            self.TextArea.insert(1.0, f.read())
            f.close()

    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:
                f = open(self.file, 'w')
                f.write(self.TextArea.get(1.0, END))
                f.close()

                self.root.title(os.path.basename(self.file) + " WritePad")
                print("File Saved")
        else:
            f = open(self.file, 'w')
            f.write(self.TextArea.get(1.0, END))
            f.close()

    def quitApp(self):
        self.root.destroy()

    def DownBar(self):
        def Bar():
            def words():
                a=Label(bar)
                word=self.TextArea.get(1.0,END)
                wordcount=len(re.findall('\w+',word))
                wordLBL.config(text=f'Words: {wordcount}')
                a.after(100,words)
            bar=Frame(self.root,relief=RIDGE,bd=4)
            bar.place(x=0,y=735,width=1522,height=30)

            wordLBL=Label(bar, text='Words:',font='times 10')
            wordLBL.place(x=10)
            words()


        Bar()


root = Tk()
YashPad = Writepad(root)
root.mainloop()
