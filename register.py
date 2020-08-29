# Importing tkinter framework
import tkinter as tk
from tkinter import *
from tkinter import ttk
# Import sqlite3
import sqlite3


def setup_db():
    # Open db
    global conn
    conn = sqlite3.connect('shengen.db')
    # Create a cursor
    global c
    c = conn.cursor()

    # Create the table if it doesn't exist
    # ID INTEGER PRIMARY KEY AUTOINCREMENT,
    try:
        c.execute("""CREATE TABLE if not exists users(
            fname TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            cPassword TEXT NOT NULL,
            sex INTEGER NOT NULL,
            country TEXT NOT NULL
            );""")

        conn.commit()

    except sqlite3.OperationalError:
        print("ERROR: Table not Created")


def submit_close():
    reg_screen.destroy()


def reg_submit():

    # Insert record into the db
    values = fname.get(), email.get(), password.get(
    ), cPassword.get(), sex.get(), country.get()

    c.execute(
        """INSERT INTO users(fname,email,password,cPassword,sex,country) VALUES (?,?, ?, ?, ?, ?
        )""", values)
    c.execute('commit')

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)

    reg_succ = Label(reg_screen, text="Registeration success! Please Wait...",
                     fg="green", font=("Calibri", 11))
    reg_succ.pack()
    reg_succ.place(x=355, y=417)
    reg_succ.after(2000, submit_close)

    c.close()
    conn.close()


def register():
    global reg_screen
    reg_screen = Toplevel(root)
    reg_screen.geometry("900x700")
    reg_screen.title("Registration Page")
    reg_screen.iconbitmap("..\Visa-Application-Management-System\icon.ico")

    global fname
    global email
    global password
    global cPassword
    global sex
    global country
    global entry_1
    global entry_2
    global entry_3
    global entry_4

    fname = StringVar()
    email = StringVar()
    password = StringVar()
    cPassword = StringVar()
    sex = IntVar()
    country = StringVar()

    Label(reg_screen, text="", bg="grey", height="2",
          width="900", font=("Calibri", 14)).pack()

    spc = Label(reg_screen, text="")
    spc.pack()
    reg_title = Label(reg_screen, text="Registration Form",
                      font=("bold", 22))
    reg_title.pack()

    label_1 = Label(reg_screen, text="FullName:", width=20, font=("bold", 10))
    label_1.place(x=195, y=130)

    entry_1 = Entry(reg_screen, width=40, textvariable=fname)
    entry_1.place(x=320, y=130)

    label_2 = Label(reg_screen, text="Email:", width=20, font=("bold", 10))
    label_2.place(x=205, y=180)

    entry_2 = Entry(reg_screen, width=40, textvariable=email)
    entry_2.place(x=320, y=180)

    label_3 = Label(reg_screen, text="Password:", width=23, font=("bold", 10))
    label_3.place(x=180, y=230)

    entry_3 = Entry(reg_screen, width=40, textvariable=password)
    entry_3.place(x=320, y=230)

    Label_6 = Label(reg_screen, text="Confirm Password:",
                    width=25, font=("bold", 10))
    Label_6.place(x=150, y=280)

    entry_4 = Entry(reg_screen, width=40, textvariable=cPassword)
    entry_4.place(x=320, y=280)

    label_4 = Label(reg_screen, text="Gender:", width=20, font=("bold", 10))
    label_4.place(x=200, y=330)
    male = Radiobutton(reg_screen, text="Male", padx=5,
                       value=1, textvariable=sex)
    male.place(x=320, y=330)
    female = Radiobutton(reg_screen, text="Female", padx=20, textvariable=sex,
                         value=2)
    female.place(x=400, y=330)
    label_5 = Label(reg_screen, text="Country", width=20, font=("bold", 10))
    label_5.place(x=200, y=380)
    list1 = ['Afghanistan', 'Angola', 'Algeria', 'Albania', 'Akrotiri', 'Armenia', 'Austria', 'Australia', 'Azerbaijan', 'American Samoa', 'Antarctica',
             'Argentina', 'Belgium', 'Borkina Faso', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Burundi', 'China', 'Canada', 'Cameroon', 'Chade',
             'Chile', 'Colombia', 'Comoros', 'Congo Democatic Republic', 'Costa Rica', 'Cape Verde', 'Crotia', 'Cuba', 'Czech Republic', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa', 'Ghana', 'Kenya', 'Germany', 'North Korea',
             'Netherland', 'Iceland', 'Poland']
    droplist = OptionMenu(reg_screen, country, *list1)
    droplist.config(width=40)
    country.set('Select Country')
    droplist.pack()
    droplist.place(x=320, y=380)
    btn_submit = Button(reg_screen, text='Submit', width=20, bg='red',
                        fg='white', font=(14), command=reg_submit)
    btn_submit.pack()
    btn_submit.place(x=360, y=470)


def log_verify():

    log_email = email_verify.get()
    log_pass = pass_verify.get()

    email_list = c.execute("SELECT email, password FROM users;")
    # "SELECT email FROM users WHERE email=(?)", (log_email,))
    conn.commit()

    for emails in email_list:

        if log_email in emails:
            if log_pass in emails:
                log_succ = Label(log_screen, text="Login Successful! \nPlease wait while we redirect you...",
                                 fg="green", font=("Calibri", 12))
                log_succ.pack()
                log_succ.place(x=330, y=400)
                log_entry_1.delete(0, END)
                log_entry_2.delete(0, END)
            else:
                log_succ = Label(log_screen, text="Failed: This User Email or Password Does Not Exist!",
                                 fg="red", font=("Calibri", 12))
                log_succ.pack()
                log_succ.place(x=280, y=150)

    # reg_succ.after(2000, submit_close)


def login():
    global log_screen
    log_screen = Toplevel(root)
    log_screen.geometry("900x700")
    log_screen.title("Login Page")
    log_screen.iconbitmap("..\Visa-Application-Management-System\icon.ico")

    Label(log_screen, text="", bg="grey", height="2",
          width="900", font=("Calibri", 14)).pack(pady=10)

    spc = Label(log_screen, text="")
    spc.pack()
    reg_title = Label(log_screen, text="Login Form",
                      font=("bold", 22))
    reg_title.pack()
    # Label(log_screen, text="").pack()
    Label(log_screen, text="Please enter your login details below").pack()

    global email_verify
    global pass_verify
    email_verify = StringVar()
    pass_verify = StringVar()

    global log_entry_1
    global log_entry_2

    label_1 = Label(log_screen, text="Email: *", width=20,
                    font=("bold", 10))
    label_1.place(x=222, y=230)

    log_entry_1 = Entry(log_screen, width=40, textvariable=email_verify)
    log_entry_1.place(x=340, y=230)

    label_2 = Label(log_screen, text="Password: *",
                    width=20, font=("bold", 10))
    label_2.place(x=222, y=280)

    log_entry_2 = Entry(log_screen, width=40, textvariable=pass_verify)
    log_entry_2.place(x=340, y=280)

    btn_submit = Button(log_screen, text='Login', width=20, bg='green',
                        fg='white', font=(14), command=log_verify)
    btn_submit.pack()
    btn_submit.place(x=360, y=340)


def window():
    global root
    root = Tk()
    root.geometry("900x700")
    root.title("Welcome Page")
    root.iconbitmap("..\Visa-Application-Management-System\icon.ico")

    Label(root, text="Welcome To Python Visa Application Portal! \n\nTo check your visa application status, file a new application or update your application, \nLogin or Create an account.",
          fg="white", bg="grey", height="6", width="900", font=("Calibri", 14)).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Button(root, text="Login", width=20, font=(
        "bold", 14), command=login).pack()
    Label(root, text="").pack()
    Button(root, text="Create Account", width=20,
           font=("bold", 14), command=register).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="Copyright 2020. All Rights Reserved \nWith Luv From Group 3",
          font=("Calibri", 8)).pack()

    root.mainloop()


setup_db()
window()
