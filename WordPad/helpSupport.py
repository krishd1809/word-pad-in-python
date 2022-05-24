from tkinter import *
from tkinter import messagebox


def HelpSupport(r,root, TextArea):
    def Q():
        def SQ():
            if WME.get()=='':
                pass
            else:
                try:
                    import smtplib

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('programers.100@gmail.com', 'smqcucdkgwmqiprp')
                    msg = f"{WME.get()}\n{AME.get(1.0,END)}"
                    server.sendmail('programers.100@gmail.com', 'yashpame@gmail.com', msg)
                    server.quit()

                    q.destroy()
                    messagebox.showinfo('SUCCESS','Query send successfully')
                except:
                    messagebox.showerror('ERROR','ERROR in sending query, Please try later or check details')


        q=Toplevel(r)
        q.title('Send Query')
        q.geometry('500x250')

        h=Label(q, text='Send Query', font='times 12 bold', bd=3, bg='white',relief=RIDGE)
        h.place(x=0,y=0,width=500,height=30)

        WM=Label(q, text='Enter Your\nMail ID', font='times 8 bold', bd=2, bg='white',relief=RIDGE)
        WM.place(x=10,y=40,width=150,height=30)
        WME = Entry(q, font='times 8 bold', bd=2)
        WME.place(x=170, y=40, width=300, height=30)

        AM = Label(q, text='Enter Your\nQuery', font='times 8 bold', bd=2, bg='white',relief=RIDGE)
        AM.place(x=10, y=80, width=150, height=30)
        AME = Text(q, font='times 8 bold', bd=2)
        AME.place(x=170, y=80, width=300, height=100)

        submitBtn=Button(q, text='Send Query', font='times 12 bold', bd=3, bg='white',command=SQ)
        submitBtn.place(x=170,y=190,width=300,height=30)


    def Fb():
        def FB():
            if WME.get() == '':
                pass
            else:
                try:
                    import smtplib

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('programers.100@gmail.com', 'smqcucdkgwmqiprp')
                    msg = f"{WME.get()}\n{AME.get(1.0, END)}"
                    server.sendmail('programers.100@gmail.com', 'yashpame@gmail.com', msg)
                    server.quit()

                    q.destroy()
                    messagebox.showinfo('SUCCESS', 'Feedback send successfully, Thanks for your Response')
                except:
                    messagebox.showerror('ERROR','ERROR in sending feedback, Please try later or check details')




        q = Toplevel(r)
        q.title('Send Feedback')
        q.geometry('500x250')

        h = Label(q, text='Send Feedback', font='times 12 bold', bd=3, bg='white', relief=RIDGE)
        h.place(x=0, y=0, width=500, height=30)

        WM = Label(q, text='Enter Your\nMail ID', font='times 8 bold', bd=2, bg='white', relief=RIDGE)
        WM.place(x=10, y=40, width=150, height=30)
        WME = Entry(q, font='times 8 bold', bd=2)
        WME.place(x=170, y=40, width=300, height=30)

        AM = Label(q, text='Enter Your\nFeedback', font='times 8 bold', bd=2, bg='white', relief=RIDGE)
        AM.place(x=10, y=80, width=150, height=30)
        AME = Text(q, font='times 8 bold', bd=2)
        AME.place(x=170, y=80, width=300, height=100)

        submitBtn = Button(q, text='Send Feedback', font='times 12 bold', bd=3, bg='white', command=FB)
        submitBtn.place(x=170, y=190, width=300, height=30)


    F = Frame(root, bd=3, relief=GROOVE)
    F.place(x=10, y=10, width=200, height=100)

    QueryBtn = Button(F, text='Send\nQuery', font='times 12 bold', bd=3, bg='white',command=Q)
    QueryBtn.place(x=10, y=10, width=80, height=70)

    FeedbackBtn = Button(F, text='Send\nFeedback', font='times 12 bold', bd=3, bg='white',command=Fb)
    FeedbackBtn.place(x=100, y=10, width=80, height=70)

