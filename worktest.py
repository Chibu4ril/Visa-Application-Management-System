from tkinter import *
from tkinter import ttk

# import sqlite3


# conn = sqlite3.connect('shengen.db')

# c = conn.cursor()

# q = c.execute(
#     "SELECT email FROM users WHERE email=('ichibuokem@gmail.com');")
# conn.commit()

# for i in q:
#     print(list(i))

def portal_start():
    portal = Toplevel(root)
    portal.title("Visa Application Form")
    portal.geometry("600x600")
    portal.iconbitmap("...\Visa-Application-Management-System\icon.ico")

    Label(portal, text="", bg="grey", height="2",
          width="900", font=("Calibri", 14)).pack(pady=10)

    spc = Label(portal, text="")
    spc.pack()

    portal_notebook = ttk.Notebook(portal)
    portal_notebook.pack()

    page1 = Frame(portal_notebook, width=600, height=600)
    page2 = Frame(portal_notebook, width=600, height=600)
    page3 = Frame(portal_notebook, width=600, height=600)
    page4 = Frame(portal_notebook, width=600, height=600)
    summary = Frame(portal_notebook, width=600, height=600)

    page1.pack(fill="both", expand=1)
    page2.pack(fill="both", expand=1)
    page3.pack(fill="both", expand=1)
    page4.pack(fill="both", expand=1)
    summary.pack(fill="both", expand=1)

    portal_notebook.add(page1, text="Basic Details")
    portal_notebook.add(page2, text="Sponsorship")
    portal_notebook.add(page3, text="Medicals")
    portal_notebook.add(page4, text="References")
    portal_notebook.add(summary, text="Summary")


# ============================================Portal End===================================================


# =============================================Instantiation window=======================================


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
        "bold", 14)).pack()
    Label(root, text="").pack()
    Button(root, text="Create Account", width=20,
           font=("bold", 14)).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="Copyright 2020. All Rights Reserved \nWith Luv From Group 3",
          font=("Calibri", 8)).pack()

    Button(root, text="Test Window", width=20,
           font=("bold", 14), command=portal_start).pack()
    Label(root, text="").pack()

    root.mainloop()


window()
