from tkinter import filedialog
from tkinter import font
from tkinter import *

root = Tk()


my_frame =Frame(root)
my_frame.pack(pady=10)

my_text =Text(my_frame, width=40, height=10, font =("Helvetica", 16), selectforeground ="black", undo= True)
my_text.pack(pady=20)

undo_button = Button(root, text="Undo", command = my_text.edit_undo)
undo_button.pack(pady=5)

redo_button = Button(root, text="Redo", command = my_text.edit_redo)
redo_button.pack(pady=5)

root.mainloop()