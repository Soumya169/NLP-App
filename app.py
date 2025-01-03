from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API

class NLPApp:
    def __init__(self):
        self.dbo = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title('NLP App')
        self.root.geometry('400x650')
        self.root.configure(bg='#1F2A44')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP App', bg='#1F2A44', fg='#FFFFFF')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Helvetica', 28, 'bold'))

        label1 = Label(self.root, text='Enter your email', bg='#1F2A44', fg='#FFFFFF')
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=40, bg='#34495E', fg='#ECF0F1', bd=0, relief="flat")
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text='Enter your password', bg='#1F2A44', fg='#FFFFFF')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=40, bg='#34495E', fg='#ECF0F1', bd=0, relief="flat", show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        login_button = Button(self.root, text='Login', width=25, height=2, bg='#2980B9', fg='white', command=self.perform_login)
        login_button.pack(pady=(20, 10))

        label3 = Label(self.root, text='Not a Member?', bg='#1F2A44', fg='#FFFFFF')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', bg='#2980B9', fg='white', command=self.register_gui)
        redirect_btn.pack(pady=(5, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP App', bg='#1F2A44', fg='#FFFFFF')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Helvetica', 28, 'bold'))

        label0 = Label(self.root, text='Enter Name', bg='#1F2A44', fg='#FFFFFF')
        label0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=40, bg='#34495E', fg='#ECF0F1', bd=0, relief="flat")
        self.name_input.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.root, text='Enter your email', bg='#1F2A44', fg='#FFFFFF')
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=40, bg='#34495E', fg='#ECF0F1', bd=0, relief="flat")
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text='Enter your password', bg='#1F2A44', fg='#FFFFFF')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=40, bg='#34495E', fg='#ECF0F1', bd=0, relief="flat", show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        register_button = Button(self.root, text='Register', width=25, height=2, bg='#2980B9', fg='white', command=self.perform_register)
        register_button.pack(pady=(20, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#1F2A44', fg='#FFFFFF')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', bg='#2980B9', fg='white', command=self.login_gui)
        redirect_btn.pack(pady=(5, 10))

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def perform_register(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('Success', 'Registration Successful')
        else:
            messagebox.showinfo('Error', 'Email Already Exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)
        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showinfo('Error', 'Incorrect Email/Password')

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP App', bg='#1F2A44', fg='#FFFFFF')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Helvetica', 28, 'bold'))

        sentiment_button = Button(self.root, text='Sentiment Analysis', width=30, height=2, bg='#2980B9', fg='white', command=self.sentiment_gui)
        sentiment_button.pack(pady=(10, 10))

        emotion_button = Button(self.root, text='Emotion Analysis', width=30, height=2, bg='#2980B9', fg='white', command=self.emotion_gui)
        emotion_button.pack(pady=(10, 10))

        logout_button = Button(self.root, text='Log Out', width=30, height=2, bg='#E74C3C', fg='white', command=self.login_gui)
        logout_button.pack(pady=(20, 20))

    def sentiment_gui(self):
        self.clear()
        self.analysis_gui('Sentiment Analysis', self.do_sentiment_analysis)

    def emotion_gui(self):
        self.clear()
        self.analysis_gui('Emotion Analysis', self.do_emotion_analysis)

    def analysis_gui(self, title, analysis_function):
        heading = Label(self.root, text='NLP App', bg='#1F2A44', fg='#FFFFFF')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Helvetica', 28, 'bold'))

        sub_heading = Label(self.root, text=title, bg='#1F2A44', fg='#FFFFFF')
        sub_heading.pack(pady=(10, 20))
        sub_heading.configure(font=('Helvetica', 20, 'bold'))

        label1 = Label(self.root, text='Enter the Text', bg='#1F2A44', fg='#FFFFFF')
        label1.pack(pady=(10, 10))

        self.analysis_input = Entry(self.root, width=40, bg='#34495E', fg='#ECF0F1', bd=0, relief="flat")
        self.analysis_input.pack(pady=(5, 10), ipady=5)

        analyze_button = Button(self.root, text='Analyze', width=20, height=2, bg='#2980B9', fg='white', command=analysis_function)
        analyze_button.pack(pady=(10, 10))

        self.analysis_result = Label(self.root, text='', bg='#1F2A44', fg='#FFFFFF')
        self.analysis_result.pack(pady=(10, 10))
        self.analysis_result.configure(font=('Helvetica', 16))

        goback_button = Button(self.root, text='Go Back', width=20, height=2, bg='#34495E', fg='white', command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.analysis_input.get()
        result = self.apio.sentiment_analysis(text)
        self.analysis_result.config(text=result)

    def do_emotion_analysis(self):
        text = self.analysis_input.get()
        result = self.apio.emotion_analysis(text)
        self.analysis_result.config(text=result)

nlp = NLPApp()
