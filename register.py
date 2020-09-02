# Importing tkinter framework
import tkinter as tk
from tkinter import *
from tkinter import ttk
# Import sqlite3
import sqlite3


# =======================================================Login & Registration=======================================

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


def login_close():
    log_screen.destroy()


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
                log_succ.after(1000, portal_start)
            else:
                log_succ = Label(log_screen, text="Failed: This User Email or Password Does Not Exist!",
                                 fg="red", font=("Calibri", 12))
                log_succ.pack()
                log_succ.place(x=280, y=150)
    log_succ.after(2000, login_close)


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

    # ==============================^^^^Login & Registration^^^^=======================================


# ============================================Portal=======================================================

def portal_start():
    portal = tk.Toplevel(root)
    portal.title("Visa Application Form")
    portal.geometry("900x900")
    # portal.iconbitmap("...\Visa-Application-Management-System\icon.ico")

    Label(portal, text="", bg="grey", height="2",
          width="900", font=("Calibri", 14)).pack(pady=10)

    # spc = Label(portal, text="")
    # spc.pack()

    portal_notebook = ttk.Notebook(portal)
    portal_notebook.pack()

    page1 = Frame(portal_notebook, width=1200, height=700)
    page2 = Frame(portal_notebook, width=1200, height=700)
    page3 = Frame(portal_notebook, width=1200, height=700)
    page4 = Frame(portal_notebook, width=1200, height=700)
    page5 = Frame(portal_notebook, width=1200, height=700)
    summary = Frame(portal_notebook, width=1200, height=700)

    page1.pack(fill="both", expand=1)
    page2.pack(fill="both", expand=1)
    page3.pack(fill="both", expand=1)
    page4.pack(fill="both", expand=1)
    page5.pack(fill="both", expand=1)
    summary.pack(fill="both", expand=1)

    portal_notebook.add(page1, text="Basic Details")
    portal_notebook.add(page2, text="Sponsorship")
    portal_notebook.add(page3, text="References")
    portal_notebook.add(page4, text="References")
    portal_notebook.add(page5, text="References")
    portal_notebook.add(summary, text="Summary")

    header = Label(page1, text="Harmonised application form",
                   font=('bold', 14))
    header.pack()
    title = Label(page1, text="Application for Schengen Visa",
                  font=('bold', 14))
    title.pack()
    subTitle = Label(page1, text="This application form is free")
    subTitle.pack()

    subTitle2 = Label(
        page1, text="Family members of EU, EEA, CH citizens shall not fill in fields no. 21, 22, 30, 31 and 32 marked with *. \nFields 1-3 shall be filled in in accordance with the data in the travel document")
    subTitle2.pack()

    # The form
    sur_label = Label(page1, text='1. Surname (Family Name): ')
    sur_label.place(x=20, y=180)
    surname = Entry(page1, width=120)
    surname.place(x=20, y=200)

    sur_label2 = Label(
        page1, text='2. Surname at birth (Former family name(s)): ')
    sur_label2.place(x=20, y=230)
    surname2 = Entry(page1, width=120)
    surname2.place(x=20, y=250)

    fname_label = Label(page1, text='3. First name(s) (Given name(s)): ')
    fname_label.place(x=20, y=280)
    fname = Entry(page1, width=120)
    fname.place(x=20, y=300)

    official = Label(page1, text='FOR OFFICIAL USE ONLY',
                     font=('Helvetica', 9, 'bold'))
    official.place(x=800, y=195)
    doa_label = Label(page1, text="Date of application: ")
    doa_label.place(x=800, y=220)
    doa_input = Entry(page1, width=30)
    doa_input.place(x=800, y=250)

    app_numLabel = Label(page1, text="Application number: ")
    app_numLabel.place(x=800, y=275)
    app_num = Entry(page1, width=30)
    app_num.place(x=800, y=300)

    # application lodged at:
    selected = IntVar()
    app_lodgedLabel = Label(page1, text="Application lodged at: ")
    app_lodgedLabel.place(x=800, y=330)
    app_lodged1 = Radiobutton(
        page1, text='Embassy/consulate', value=1, variable=selected)
    app_lodged2 = Radiobutton(
        page1, text='Service provider', value=2, variable=selected)
    app_lodged3 = Radiobutton(
        page1, text='Commercial intermediary', value=3, variable=selected)
    app_lodged4 = Radiobutton(
        page1, text='Border (Name):', value=4, variable=selected)
    app_lodged4a = Entry(page1, width=30)
    app_lodged5 = Radiobutton(
        page1, text='Other:', value=5, variable=selected)
    app_lodged1.place(x=800, y=360)
    app_lodged2.place(x=800, y=410)
    app_lodged3.place(x=800, y=460)
    app_lodged4.place(x=800, y=510)
    app_lodged4a.place(x=800, y=530)
    app_lodged5.place(x=800, y=550)

    # date of birth( can be mordified)

    dob_label = Label(page1, text="4. Date of birth(day-month-year): ")
    dob_label.place(x=20, y=330)
    dob = Entry(page1, width=30)
    dob.place(x=20, y=350)

    pob_label = Label(page1, text="5. Place of birth: ")
    pob_label.place(x=250, y=330)
    pob = Entry(page1, width=35)
    pob.place(x=250, y=350)

    cob_label = Label(page1, text="6. Country of birth: ")
    cob_label.place(x=250, y=380)
    cob = Entry(page1, width=35)
    cob.place(x=250, y=400)

    cn_label = Label(page1, text="7. Current nationality: ")
    cn_label.place(x=500, y=330)
    cn = Entry(page1, width=35)
    cn.place(x=500, y=350)

    nab_label = Label(page1, text=" Nationality at birth if different : ")
    nab_label.place(x=500, y=380)
    nab = Entry(page1, width=35)
    nab.place(x=500, y=400)

    cn_label = Label(page1, text=" Other nationality: ")
    cn_label.place(x=500, y=430)
    cn = Entry(page1, width=35)
    cn.place(x=500, y=450)

    selected = IntVar()

    rad_label = Label(page1, text=" 8. Sex: ")
    rad_label.place(x=20, y=480)
    rad1 = Radiobutton(page1, text='Male', value=1, variable=selected)
    rad2 = Radiobutton(page1, text='Female', value=2, variable=selected)
    rad1.place(x=20, y=500)
    rad2.place(x=100, y=500)

    selected = IntVar()

    rad_status_label = Label(page1, text=" 9. Civil status: ")
    rad_status_label.place(x=250, y=480)
    rad_status1 = Radiobutton(
        page1, text='Single', value=1, variable=selected)
    rad_status2 = Radiobutton(
        page1, text='Married', value=2, variable=selected)
    rad_status3 = Radiobutton(
        page1, text='Registered Partnership', value=3, variable=selected)
    rad_status4 = Radiobutton(
        page1, text='Seperated', value=4, variable=selected)
    rad_status5 = Radiobutton(
        page1, text='Divorced', value=5, variable=selected)
    rad_status6 = Radiobutton(
        page1, text='Widow(er)', value=6, variable=selected)
    rad_status7 = Radiobutton(
        page1, text='Other (please specify)', value=7, variable=selected)
    rad_status1.place(x=250, y=500)
    rad_status2.place(x=350, y=500)
    rad_status3.place(x=450, y=500)
    rad_status4.place(x=610, y=500)
    rad_status5.place(x=250, y=520)
    rad_status6.place(x=350, y=520)
    rad_status7.place(x=480, y=520)

#    ---------------------------------------------------------------
    # button to show frame 2 with text
    # layout2
    button1 = Button(page1, text="Logout", fg="white",
                     bg="red", width=20).place(x=300, y=650)
    button2 = Button(page1, text="Page 2", fg="white",
                     bg="blue", width=20).place(x=470, y=650)

    # -------------------------------------------------------------

    header = Label(page2, text="Harmonised application form",
                   font=('bold', 14))
    header.pack()
    title = Label(page2, text="Application for Schengen Visa",
                  font=('bold', 14))
    title.pack()
    subTitle = Label(page2, text="This application form is free")
    subTitle.pack()

    parental_aut_label = Label(
        page2, text="10. parental authority(in case of minors)/legal guardian(surname, first name, address, if different \nfrom applicant's, telephoneno., e-mail address, and nationality): ")
    parental_aut_label.place(x=20, y=130)
    parental_aut = Entry(page2, width=120)
    parental_aut.place(x=20, y=170)

    National_ID_label = Label(
        page2, text="11. National identity, where applicable: ")
    National_ID_label.place(x=20, y=200)
    National_ID = Entry(page2, width=40)
    National_ID.place(x=40, y=240)

    # Should Be In Summary Page ===========
    supporting_docLabel = Label(page2, text="Supporting documents: ")
    rad1 = Radiobutton(page2, text='Travel document', value=1)
    rad2 = Radiobutton(page2, text='Proof of funds', value=2)
    rad3 = Radiobutton(page2, text='Invitation', value=3)
    supporting_docLabel.place(x=850, y=130)
    rad1.place(x=850, y=150)
    rad2.place(x=850, y=180)
    rad3.place(x=850, y=210)

# Summary page==============

    Travel_doc_label = Label(page2, text="12. Type of travel document: ")
    rad1 = Radiobutton(page2, text='Ordinary passport', value=1)
    rad2 = Radiobutton(page2, text='Diplomatic passport', value=2)
    rad3 = Radiobutton(page2, text='Service passport', value=3)
    rad4 = Radiobutton(page2, text='Official passport', value=4)
    rad5 = Radiobutton(page2, text='Special passport', value=5)
    rad6 = Radiobutton(
        page2, text='Other travel document(please specify)', value=6)
    Travel_doc_label.place(x=20, y=270)
    rad1.place(x=40, y=290)
    rad2.place(x=170, y=290)
    rad3.place(x=310, y=290)
    rad4.place(x=430, y=290)
    rad5.place(x=40, y=320)
    rad6.place(x=170, y=320)

    num_doc_label = Label(
        page2, text="13. National identity, where applicable: ")
    num_doc_label.place(x=20, y=350)
    num_doc = Entry(page2, width=30)
    num_doc.place(x=40, y=380)
    num_doc_label = Label(page2, text="14. Date of issue: ")
    num_doc_label.place(x=250, y=350)
    num_doc = Entry(page2, width=30)
    num_doc.place(x=250, y=380)
    num_doc_label = Label(page2, text="15. Valid until: ")
    num_doc_label.place(x=450, y=350)
    num_doc = Entry(page2, width=30)
    num_doc.place(x=450, y=380)
    num_doc_label = Label(page2, text="16. Issued by (Country): ")
    num_doc_label.place(x=650, y=350)
    num_doc = Entry(page2, width=30)
    num_doc.place(x=650, y=380)

    family_mem_label = Label(page2,
                             text="17. Personal data of family member who is an EU, EEA or CH citizen (if applicable) ")
    family_mem_label.place(x=20, y=410)
    sur_label = Label(page2, text='Surname (Family Name): ')
    sur_label.place(x=40, y=440)
    surname = Entry(page2, width=25)
    surname.place(x=260, y=440)
    first_nam_label = Label(page2, text='First name(s) (Given Name(s)): ')
    first_nam_label.place(x=450, y=440)
    first_name = Entry(page2, width=35)
    first_name.place(x=620, y=440)
    DOBlabel = Label(page2, text='Date of birth (day-month-year): ')
    DOBlabel.place(x=40, y=480)
    DOBname = Entry(page2, width=25)
    DOBname.place(x=260, y=480)
    Nationality_label = Label(page2, text='Nationality: ')
    Nationality_label.place(x=450, y=480)
    Nationality_name = Entry(page2, width=35)
    Nationality_name.place(x=620, y=480)
    Nationality_label = Label(
        page2, text='Number of travel document or ID card: ')
    Nationality_label.place(x=40, y=510)
    Nationality_name = Entry(page2, width=25)
    Nationality_name.place(x=260, y=510)

    family_rship_label = Label(
        page2, text="18. Family relationship with an EU, EEA or CH citizen (if applicable) ")
    family_rship_label.place(x=20, y=540)
    rad1 = Radiobutton(page2, text='Spouse', value=1)
    rad2 = Radiobutton(page2, text='Child', value=2)
    rad3 = Radiobutton(page2, text='Grandchild', value=3)
    rad4 = Radiobutton(page2, text='Dependent ascendent', value=4)
    rad5 = Radiobutton(page2, text='Registered partnership', value=5)
    rad6 = Radiobutton(page2, text='Other', value=6)
    rad1.place(x=40, y=570)
    rad2.place(x=110, y=570)
    rad3.place(x=180, y=570)
    rad4.place(x=280, y=570)
    rad5.place(x=420, y=570)
    rad6.place(x=570, y=570)
    home_add_label = Label(
        page2, text="19. Applicant's home address and e-mail address: ")
    home_add_label.place(x=20, y=600)
    home_add = Entry(page2, width=25)
    home_add.place(x=290, y=600)
    tel_label = Label(page2, text='Telephone no.: (Family Name): ')
    tel_label.place(x=450, y=600)
    telephone = Entry(page2, width=30)
    telephone.place(x=620, y=600)

    button1 = ttk.Button(page2, text="Page 1",
                         command=lambda: controller.show_frame(Page1)).place(x=350, y=650)
    button2 = ttk.Button(page2, text="Page3",
                         command=lambda: controller.show_frame(Page3)).place(x=450, y=650)

# ------------------------------------------------------

    header = Label(page3, text="Harmonised application form",
                   font=('bold', 14))
    header.pack()
    title = Label(page3, text="Application for Schengen Visa",
                  font=('bold', 14))
    title.pack()
    subTitle = Label(page3, text="This application form is free")
    subTitle.pack()

    home_add_label = Label(
        page3, text="20. Residence in a country other than the country of current nationality: ")
    home_add_label.place(x=20, y=130)
    rad1 = Radiobutton(page3, text='No', value=1)
    rad2 = Radiobutton(page3,
                       text='Yes. Residence permit or equivalent ....................... No. .................... Valid until ........................',
                       value=2)
    rad3 = Radiobutton(page3, text='Means of \n transportation', value=3)
    rad4 = Radiobutton(page3, text='Other', value=4)
    visa_decLabel = Label(page3, text="Visa decision: ")
    rad5 = Radiobutton(page3, text='Refund', value=5)
    rad6 = Radiobutton(page3, text='Issued', value=6)
    visa_validLabel = Label(page3, text="Visa valid: ")
    rad7 = Radiobutton(page3, text='From', value=7)
    rad8 = Radiobutton(page3, text='Until', value=8)
    rad1.place(x=20, y=160)
    rad2.place(x=80, y=160)
    rad3.place(x=850, y=240)
    rad4.place(x=850, y=280)
    visa_decLabel.place(x=850, y=340)
    rad5.place(x=850, y=370)
    rad6.place(x=850, y=400)
    visa_validLabel.place(x=850, y=440)
    rad7.place(x=850, y=470)
    rad8.place(x=850, y=500)
    Occ_label = Label(page3, text="21. Current occupation: ")
    Occ_label.place(x=20, y=190)
    occ = Entry(page3, width=25)
    occ.place(x=200, y=190)
    Emp_add_label = Label(page3,
                          text="22. Employer and Employer's address and telephone number. For students; name and address of educational establishment: ")
    Emp_add_label.place(x=20, y=220)
    occ = Entry(page3, width=60)
    occ.place(x=40, y=250)
    pur_label = Label(page3, text="23. Purpose(s) of the journey: ")
    pur_label.place(x=20, y=275)
    rad1 = Radiobutton(page3, text='Tourism', value=1)
    rad2 = Radiobutton(page3, text='Business', value=2)
    rad3 = Radiobutton(page3, text='Visiting family or friends', value=3)
    rad4 = Radiobutton(page3, text='Cultural', value=4)
    rad5 = Radiobutton(page3, text='Sports', value=5)
    rad6 = Radiobutton(page3, text='Official visit', value=6)
    rad7 = Radiobutton(page3, text='Medical reasons', value=7)
    rad8 = Radiobutton(page3, text='Study', value=8)
    rad1.place(x=20, y=300)
    rad2.place(x=90, y=300)
    rad3.place(x=160, y=300)
    rad4.place(x=320, y=300)
    rad5.place(x=400, y=300)
    rad6.place(x=460, y=300)
    rad7.place(x=550, y=300)
    rad8.place(x=670, y=300)

    add_info_label = Label(
        page3, text="24. Additional information on purpose of stay: ")
    add_info_label.place(x=20, y=330)

    add_info = Entry(page3, width=90)
    add_info.place(x=300, y=330)

    mem_state_label = Label(page3,
                            text="25. Member State of main destination (and other \n     Member States of destination , if applicable): ")
    mem_state_label.place(x=20, y=360)

    mem_state = Entry(page3, width=30)
    mem_state.place(x=300, y=360)

    mem_state2_label = Label(
        page3, text='26. Member State of first entry:')
    mem_state2_label.place(x=500, y=360)

    mem_state = Entry(page3, width=28)
    mem_state.place(x=673, y=360)

    num_entries_label = Label(
        page3, text='27. Number of entries requested:')
    num_entries_label.place(x=20, y=400)

    rad1 = Radiobutton(page3, text='Single entry', value=1)
    rad2 = Radiobutton(page3, text='Two entries', value=2)
    rad3 = Radiobutton(page3, text='Multiple entries', value=3)

    rad1.place(x=20, y=430)
    rad2.place(x=120, y=430)
    rad3.place(x=220, y=430)

    int_doa_label = Label(
        page3, text='Intended date of arrival of the first intended stay in the Schengen area:')
    int_doa_label.place(x=340, y=400)

    arr_date = Entry(page3, width=15)
    arr_date.place(x=750, y=400)

    num_entries_label = Label(page3,
                              text='Intended date of departure from the Schengen area after first intended stay:')
    num_entries_label.place(x=340, y=430)

    dep_date = Entry(page3, width=15)
    dep_date.place(x=750, y=430)

    fingerprint_label = Label(page3,
                              text='28. Fingerprints collected previously for the purpose of applying for a Schengen visa:')
    fingerprint_label.place(x=20, y=460)

    rad1 = Radiobutton(page3, text='Yes', value=1)
    rad2 = Radiobutton(page3, text='No', value=2)

    rad1.place(x=480, y=460)
    rad2.place(x=530, y=460)

    fingerprint_label = Label(page3,
                              text='Date,  if known ........................................... Visa sticker number, if known   ............................................:')
    fingerprint_label.place(x=40, y=480)

    entry_per_label = Label(
        page3, text='29. Entry permit for final country of destination, where applicable: ')
    entry_per_label.place(x=20, y=500)

    issuedby_label = Label(page3,
                           text='Issued by  ........................................... Valid from ............................................ until .........................:')
    issuedby_label.place(x=40, y=530)

    surname_label = Label(page3,
                          text='30. Surname and firstname of the inviting person(s) in the Member State(s). if not applicable, name of hotel(s) or temporary accommodation(s) in the Member State(s):')
    surname_label.place(x=20, y=560)

    surname = Entry(page3, width=100)
    surname.place(x=40, y=580)

    entry_per_label = Label(page3,
                            text=' Address and e-mail address of inviting person(s)/hotel(s)/temporary accomodation(s): ')
    entry_per_label.place(x=35, y=600)

    surname = Entry(page3, width=60)
    surname.place(x=500, y=600)

    phone_label = Label(page3, text=' Telephone no.: ')
    phone_label.place(x=35, y=630)

    surname = Entry(page3, width=60)
    surname.place(x=180, y=630)

    button1 = ttk.Button(page3, text="Page 2",
                         command=lambda: controller.show_frame(Page2)).place(x=350, y=660)
    button2 = ttk.Button(page3, text="Page4",
                         command=lambda: controller.show_frame(Page4)).place(x=450, y=660)

    # ==========================================

    header = Label(page4, text="Harmonised application form",
                   font=('bold', 14))
    header.pack()
    title = Label(page4, text="Application for Schengen Visa",
                  font=('bold', 14))
    title.pack()
    subTitle = Label(page4, text="This application form is free")
    subTitle.pack()

    name_add_label = Label(
        page4, text='31. Name and address of inviting company/organisation: ')
    name_add_label.place(x=20, y=90)

    name = Entry(page4, width=60)
    name.place(x=500, y=90)

    sur_name_label = Label(page4,
                           text=' Surname, firstname, address, telephone no. and e-mail address of contact person in company/organisation: ')
    sur_name_label.place(x=35, y=120)

    surname = Entry(page4, width=42)
    surname.place(x=610, y=120)

    phone_label = Label(
        page4, text=' Telephone no. of company/organisation: ')
    phone_label.place(x=35, y=150)

    surname = Entry(page4, width=60)
    surname.place(x=500, y=150)

    travel_cost_label = Label(page4,
                              text='32. Cost of travelling and living during the applicant''s stay is covered: ')
    travel_cost_label.place(x=20, y=175)

    name = Entry(page4, width=60)
    name.place(x=500, y=175)

    rad1 = Radiobutton(
        page4, text='by the applicant himself/herself', value=1)
    rad1.place(x=35, y=195)

    phone_label = Label(page4, text=' Means of support: ')
    phone_label.place(x=35, y=225)

    rad1 = Radiobutton(page4, text='Cash', value=1)
    rad2 = Radiobutton(page4, text='Travellers cheques', value=2)
    rad3 = Radiobutton(page4, text='Credit card', value=3)
    rad4 = Radiobutton(page4, text='Pre-paid accomodation', value=4)

    rad1.place(x=35, y=240)
    rad2.place(x=100, y=240)
    rad3.place(x=230, y=240)
    rad4.place(x=330, y=240)

    rad5 = Radiobutton(page4, text='Pre-paid transport', value=5)
    rad6 = Radiobutton(page4, text='Other (please specify):', value=6)
    rad7 = Radiobutton(
        page4, text='by a sponsor(host, company, organisation) please specify:', value=7)
    rad8 = Radiobutton(page4,
                       text='..................................................... refered to in field 30 or 31 ...................................... other (please specify):',
                       value=8)
    rad5.place(x=35, y=260)
    rad6.place(x=160, y=260)
    rad7.place(x=35, y=290)
    rad8.place(x=35, y=290)

    specify = Entry(page4, width=50)
    specify.place(x=600, y=320)

    phone_label = Label(page4, text=' Means of support: ')
    phone_label.place(x=35, y=340)

    rad1 = Radiobutton(page4, text='Cash', value=1)
    rad2 = Radiobutton(page4, text='Accomodation provided', value=2)
    rad3 = Radiobutton(
        page4, text='All expenses covered during the stay', value=3)
    rad4 = Radiobutton(page4, text='Pre-paid transport', value=4)
    rad5 = Radiobutton(page4, text='Other (please specify)', value=5)

    rad1.place(x=35, y=345)
    rad2.place(x=95, y=345)
    rad3.place(x=260, y=345)
    rad4.place(x=480, y=345)
    rad5.place(x=605, y=345)

    other = Entry(page4, width=18)
    other.place(x=750, y=345)

    Button(page4, text='Home', width=20, bg='blue',
           fg='white').place(x=35, y=470)
    Button(page4, text='Submit', width=20, bg='red',
           fg='white').place(x=750, y=470)

    # button1 = ttk.Button(page3, text="Page 2",
    #                      command=lambda: controller.show_frame(Page2)).place(x=350, y=680)
    # button2 = ttk.Button(page3, text="Page4",
    #                      command=lambda: controller.show_frame(Page4)).place(x=450, y=680)


# -----------------------------Summary-----------------------

    # label = Label(summary, text="Summary", font=LARGEFONT)
    # label.grid(row=0, column=4)

    # Button(summary, text='Submit', width=20, bg='brown',
    #        fg='white').place(x=230, y=470)
    # button1 = Button(summary, text="Page 4",
    #                  command=lambda: controller.show_frame(Page4)).place(x=350, y=680)
    # button2 = Button(summary, text="Login",
    #                  command=lambda: controller.show_frame(StartPage)).place(x=450, y=680)


# ============================================Portal End===================================================


# =============================================Instantiation window=======================================


def window():
    global root
    root = Tk()
    root.geometry("700x500")
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
