from tkinter import *

root= Tk()
root.geometry("500x600")

my_frame =Frame(root)
my_frame.pack(pady=10)

my_text =Text(my_frame, width=40, height=10, font =("Helvetica", 16), selectforeground ="black", undo= True)
my_text.pack()


def add_image():
    global my_image
    my_image = PhotoImage(file = "a.png")
    position = my_text.index(INSERT)
    my_text.image_create(END, image=my_image)
    my_label.config(text=position)

image_button = Button(root, text="Add Image", command = add_image)
image_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack()

root.mainloop()