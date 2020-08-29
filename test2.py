import tkinter as tk
from tkinter import *
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

   # _init_ function for class tkinterApp
    def _init_(self, *args, **kwargs):
        # _init_ function for class Tk
        tk.Tk._init_(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Reg_page, Page1, Page2, Page3, Page4, Summary):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        # to display the current frame passed as

    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage


class StartPage(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
# CODE FOR LOGIN PAGE
      # CODE FOR DATABASE
        UsernameOREmail = StringVar()
        Password = StringVar()
        var = IntVar()
        c = StringVar()
        var1 = IntVar()

        def database():
            Username = UsernameOREmail.get()
            Passcode = Password.get()
            conn = sqlite3.connect('Login_Form.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
            cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',
                           (Username, Passcode))
            conn.commit()

        # CODE FOR LOGIN PAGE CONTENT

        label_0 = Label(self, text="Login Page", width=20, font=("bold", 20))
        label_0.place(x=150, y=53)

        label_1 = Label(self, text="Username/Email",
                        width=20, font=("bold", 10))
        label_1.place(x=75, y=130)

        entry_1 = Entry(self, textvar=UsernameOREmail)
        entry_1.place(x=240, y=130)

        label_2 = Label(self, text="Password", width=20, font=("bold", 10))
        label_2.place(x=58, y=180)

        entry_2 = Entry(self, textvar=Password)
        entry_2.place(x=240, y=180)

        button1 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(Reg_page)).place(x=240, y=250)


class Reg_page(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)

        # CODE FOR REGISTRATION PAGE
        # CODE FOR DATABASE
        Fullname = StringVar()
        Email = StringVar()
        Password = StringVar()
        ConfirmPassword = StringVar()
        var = IntVar()
        c = StringVar()
        var1 = IntVar()

        def database():
            name1 = Fullname.get()
            email = Email.get()
            gender = var.get()
            country = c.get()
            prog = var1.get()
            conn = sqlite3.connect('Form24.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
            cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',
                           (name1, email, gender, country, prog,))
            conn.commit()

        label_0 = Label(self, text="Registration form",
                        width=20, font=("bold", 30))
        label_0.place(x=150, y=53)

        label_1 = Label(self, text="FullName", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        entry_1 = Entry(self, textvar=Fullname)
        entry_1.place(x=240, y=130)

        label_2 = Label(self, text="Email", width=20, font=("bold", 10))
        label_2.place(x=68, y=180)

        entry_2 = Entry(self, textvar=Email)
        entry_2.place(x=240, y=180)

        label_3 = Label(self, text="Password", width=23, font=("bold", 10))
        label_3.place(x=68, y=230)

        entry_3 = Entry(self, textvar=Password)
        entry_3.place(x=240, y=230)

        Label_6 = Label(self, text="Confirm Password",
                        width=25, font=("bold", 10))
        Label_6.place(x=80, y=280)

        entry_4 = Entry(self, textvar="Confirm Password")
        entry_4.place(x=330, y=280)

        label_4 = Label(self, text="Gender", width=20, font=("bold", 10))
        label_4.place(x=68, y=330)

        Radiobutton(self, text="Male", padx=5, variable=var,
                    value=1).place(x=240, y=330)
        Radiobutton(self, text="Female", padx=20,
                    variable=var, value=2).place(x=320, y=330)

        label_5 = Label(self, text="country", width=20, font=("bold", 10))
        label_5.place(x=68, y=380)

        list1 = ['Afghanistan', 'Angola', 'Algeria', 'Albania', 'Akrotiri', 'Armenia', 'Austria', 'Australia',
                 'Azerbaijan', 'American Samoa', 'Antarctica',
                 'Argentina', 'Belgium', 'Borkina Faso', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria',
                 'Burundi', 'China', 'Canada', 'Cameroon', 'Chade',
                 'Chile', 'Colombia', 'Comoros', 'Congo Democatic Republic', 'Costa Rica', 'Cape Verde', 'Crotia',
                 'Cuba', 'Czech Republic', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa', 'Ghana', 'Kenya',
                 'Germany', 'North Korea',
                 'Netherland', 'Iceland', 'Poland']

        droplist = OptionMenu(self, c, *list1)
        droplist.config(width=15)
        c.set('select your country')
        droplist.place(x=240, y=380)

        Button(self, text='Submit', width=20, bg='brown',
               fg='white', command=database).place(x=230, y=470)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="login",
                             command=lambda: controller.show_frame(StartPage)).place(x=350, y=650)
        button2 = ttk.Button(self, text="page1",
                             command=lambda: controller.show_frame(Page1)).place(x=450, y=650)

# CODE FOR PAGE 1 FORM


class Page1(tk.Frame):

    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)

        # The headers and titles
        header = ttk.Label(
            self, text="Harmonised application form", font=('bold', 14))
        header.place(x=20, y=20)
        title = ttk.Label(self, text="Application for Schengen Visa",
                          font=('bold', 14))
        title.place(x=20, y=50)
        subTitle = ttk.Label(self, text="This application form is free")
        subTitle.place(x=20, y=80)

        subTitle2 = ttk.Label(
            self, text="Family members of EU, EEA, CH citizens shall not fill in fields no. 21, 22, 30, 31 and 32 marked with *. \nFields 1-3 shall be filled in in accordance with the data in the travel document")
        subTitle2.place(x=20, y=110)

        # The form
        sur_label = Label(self, text='1. Surname (Family Name): ')
        sur_label.place(x=20, y=180)
        surname = Entry(self, width=120)
        surname.place(x=20, y=200)

        sur_label2 = Label(
            self, text='2. Surname at birth (Former family name(s)): ')
        sur_label2.place(x=20, y=230)
        surname2 = Entry(self, width=120)
        surname2.place(x=20, y=250)

        fname_label = Label(self, text='3. First name(s) (Given name(s)): ')
        fname_label.place(x=20, y=280)
        fname = Entry(self, width=120)
        fname.place(x=20, y=300)

        official = Label(self, text='FOR OFFICIAL USE ONLY',
                         font=('Helvetica', 9, 'bold'))
        official.place(x=800, y=195)
        doa_label = Label(self, text="Date of application: ")
        doa_label.place(x=800, y=220)
        doa_input = Entry(self, width=30)
        doa_input.place(x=800, y=250)

        app_numLabel = Label(self, text="Application number: ")
        app_numLabel.place(x=800, y=275)
        app_num = Entry(self, width=30)
        app_num.place(x=800, y=300)

        # application lodged at:
        selected = IntVar()
        app_lodgedLabel = Label(self, text="Application lodged at: ")
        app_lodgedLabel.place(x=800, y=330)
        app_lodged1 = Radiobutton(
            self, text='Embassy/consulate', value=1, variable=selected)
        app_lodged2 = Radiobutton(
            self, text='Service provider', value=2, variable=selected)
        app_lodged3 = Radiobutton(
            self, text='Commercial intermediary', value=3, variable=selected)
        app_lodged4 = Radiobutton(
            self, text='Border (Name):', value=4, variable=selected)
        app_lodged4a = Entry(self, width=30)
        app_lodged5 = Radiobutton(
            self, text='Other:', value=5, variable=selected)
        app_lodged1.place(x=800, y=360)
        app_lodged2.place(x=800, y=410)
        app_lodged3.place(x=800, y=460)
        app_lodged4.place(x=800, y=510)
        app_lodged4a.place(x=800, y=530)
        app_lodged5.place(x=800, y=550)

        # date of birth( can be mordified)

        dob_label = Label(self, text="4. Date of birth(day-month-year): ")
        dob_label.place(x=20, y=330)
        dob = Entry(self, width=30)
        dob.place(x=20, y=350)

        pob_label = Label(self, text="5. Place of birth: ")
        pob_label.place(x=250, y=330)
        pob = Entry(self, width=35)
        pob.place(x=250, y=350)

        cob_label = Label(self, text="6. Country of birth: ")
        cob_label.place(x=250, y=380)
        cob = Entry(self, width=35)
        cob.place(x=250, y=400)

        cn_label = Label(self, text="7. Current nationality: ")
        cn_label.place(x=500, y=330)
        cn = Entry(self, width=35)
        cn.place(x=500, y=350)

        nab_label = Label(self, text=" Nationality at birth if different : ")
        nab_label.place(x=500, y=380)
        nab = Entry(self, width=35)
        nab.place(x=500, y=400)

        cn_label = Label(self, text=" Other nationality: ")
        cn_label.place(x=500, y=430)
        cn = Entry(self, width=35)
        cn.place(x=500, y=450)

        selected = IntVar()

        rad_label = Label(self, text=" 8. Sex: ")
        rad_label.place(x=20, y=480)
        rad1 = Radiobutton(self, text='Male', value=1, variable=selected)
        rad2 = Radiobutton(self, text='Female', value=2, variable=selected)
        rad1.place(x=20, y=500)
        rad2.place(x=100, y=500)

        selected = IntVar()

        rad_status_label = Label(self, text=" 9. Civil status: ")
        rad_status_label.place(x=250, y=480)
        rad_status1 = Radiobutton(
            self, text='Single', value=1, variable=selected)
        rad_status2 = Radiobutton(
            self, text='Married', value=2, variable=selected)
        rad_status3 = Radiobutton(
            self, text='Registered Partnership', value=3, variable=selected)
        rad_status4 = Radiobutton(
            self, text='Seperated', value=4, variable=selected)
        rad_status5 = Radiobutton(
            self, text='Divorced', value=5, variable=selected)
        rad_status6 = Radiobutton(
            self, text='Widow(er)', value=6, variable=selected)
        rad_status7 = Radiobutton(
            self, text='Other (please specify)', value=7, variable=selected)
        rad_status1.place(x=250, y=500)
        rad_status2.place(x=350, y=500)
        rad_status3.place(x=450, y=500)
        rad_status4.place(x=610, y=500)
        rad_status5.place(x=250, y=520)
        rad_status6.place(x=350, y=520)
        rad_status7.place(x=480, y=520)

        parental_aut_label = Label(
            self, text="10. parental authority(in case of minors)/legal guardian(surname, first name, address, if different \nfrom applicant's, telephoneno., e-mail address, and nationality): ")
        parental_aut_label.place(x=20, y=570)
        parental_aut = Entry(self, width=120)
        parental_aut.place(x=20, y=590)
        parental_aut2 = Entry(self, width=120)
        parental_aut2.place(x=20, y=620)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Logout",
                             command=lambda: controller.show_frame(StartPage)).place(x=350, y=650)
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2)).place(x=450, y=650)

    # third window frame page2

# CODE FOR PAGE2(CONTINUATION OF PAGE 1 FORM)


class Page2(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
       # The headers and titles

        header = Label(self, text="Harmonised application form",
                       font=('bold', 14))
        header.place(x=400, y=20)
        title = Label(self, text="Application for Schengen Visa",
                      font=('bold', 14))
        title.place(x=400, y=50)
        subTitle = Label(self, text="This application form is free")
        subTitle.place(x=450, y=80)

        page_label = Label(self, text="page 2: ")
        page_label.place(x=920, y=30)

        National_ID_label = Label(
            self, text="11. National identity, where applicable: ")
        National_ID_label.place(x=20, y=130)
        National_ID = Entry(self, width=40)
        National_ID.place(x=40, y=150)

        supporting_docLabel = Label(self, text="Supporting documents: ")
        rad1 = Radiobutton(self, text='Travel document', value=1)
        rad2 = Radiobutton(self, text='Proof of funds', value=2)
        rad3 = Radiobutton(self, text='Invitation', value=3)

        supporting_docLabel.place(x=850, y=130)
        rad1.place(x=850, y=150)
        rad2.place(x=850, y=180)
        rad3.place(x=850, y=210)

        Travel_doc_label = Label(self, text="12. Type of travel document: ")
        rad1 = Radiobutton(self, text='Ordinary passport', value=1)
        rad2 = Radiobutton(self, text='Diplomatic passport', value=2)
        rad3 = Radiobutton(self, text='Service passport', value=3)
        rad4 = Radiobutton(self, text='Official passport', value=4)
        rad5 = Radiobutton(self, text='Special passport', value=5)
        rad6 = Radiobutton(
            self, text='Other travel document(please specify)', value=6)

        Travel_doc_label.place(x=20, y=180)
        rad1.place(x=40, y=200)
        rad2.place(x=170, y=200)
        rad3.place(x=310, y=200)
        rad4.place(x=430, y=200)
        rad5.place(x=40, y=220)
        rad6.place(x=170, y=220)

        num_doc_label = Label(
            self, text="13. National identity, where applicable: ")
        num_doc_label.place(x=20, y=250)
        num_doc = Entry(self, width=30)
        num_doc.place(x=40, y=280)

        num_doc_label = Label(self, text="14. Date of issue: ")
        num_doc_label.place(x=245, y=250)
        num_doc = Entry(self, width=30)
        num_doc.place(x=245, y=280)

        num_doc_label = Label(self, text="15. Valid until: ")
        num_doc_label.place(x=450, y=250)
        num_doc = Entry(self, width=30)
        num_doc.place(x=450, y=280)

        num_doc_label = Label(self, text="16. Issued by (Country): ")
        num_doc_label.place(x=650, y=250)
        num_doc = Entry(self, width=30)
        num_doc.place(x=650, y=280)

        family_mem_label = Label(self,
                                 text="17. Personal data of family member who is an EU, EEA or CH citizen (if applicable) ")
        family_mem_label.place(x=20, y=310)

        sur_label = Label(self, text='Surname (Family Name): ')
        sur_label.place(x=40, y=330)
        surname = Entry(self, width=25)
        surname.place(x=260, y=330)

        first_nam_label = Label(self, text='First name(s) (Given Name(s)): ')
        first_nam_label.place(x=450, y=330)
        first_name = Entry(self, width=35)
        first_name.place(x=620, y=330)

        DOB_label = Label(self, text='Date of birth (day-month-year): ')
        DOB_label.place(x=40, y=360)
        DOB_name = Entry(self, width=25)
        DOB_name.place(x=260, y=360)

        Nationality_label = Label(self, text='Nationality: ')
        Nationality_label.place(x=450, y=360)
        Nationality_name = Entry(self, width=35)
        Nationality_name.place(x=620, y=360)

        Nationality_label = Label(
            self, text='Number of travel document or ID card: ')
        Nationality_label.place(x=40, y=390)
        Nationality_name = Entry(self, width=25)
        Nationality_name.place(x=260, y=390)

        family_rship_label = Label(
            self, text="18. Family relationship with an EU, EEA or CH citizen (if applicable) ")
        family_rship_label.place(x=20, y=420)

        rad1 = Radiobutton(self, text='Spouse', value=1)
        rad2 = Radiobutton(self, text='Child', value=2)
        rad3 = Radiobutton(self, text='Grandchild', value=3)
        rad4 = Radiobutton(self, text='Dependent ascendent', value=4)
        rad5 = Radiobutton(self, text='Registered partnership', value=5)
        rad6 = Radiobutton(self, text='Other', value=6)

        rad1.place(x=40, y=440)
        rad2.place(x=110, y=440)
        rad3.place(x=180, y=440)
        rad4.place(x=280, y=440)
        rad5.place(x=420, y=440)
        rad6.place(x=570, y=440)

        home_add_label = Label(
            self, text="19. Applicant's home address and e-mail address: ")
        home_add_label.place(x=20, y=470)

        home_add = Entry(self, width=25)
        home_add.place(x=290, y=470)

        tel_label = Label(self, text='Telephone no.: (Family Name): ')
        tel_label.place(x=450, y=470)
        telephone = Entry(self, width=30)
        telephone.place(x=620, y=470)

        home_add_label = Label(
            self, text="20. Residence in a country other than the country of current nationality: ")
        home_add_label.place(x=20, y=500)

        rad1 = Radiobutton(self, text='No', value=1)
        rad2 = Radiobutton(self,
                           text='Yes. Residence permit or equivalent ....................... No. .................... Valid until ........................',
                           value=2)
        rad3 = Radiobutton(self, text='Means of \n transportation', value=3)
        rad4 = Radiobutton(self, text='Other', value=4)
        visa_decLabel = Label(self, text="Visa decision: ")
        rad5 = Radiobutton(self, text='Refund', value=5)
        rad6 = Radiobutton(self, text='Issued', value=6)
        visa_validLabel = Label(self, text="Visa valid: ")
        rad7 = Radiobutton(self, text='From', value=7)
        rad8 = Radiobutton(self, text='Until', value=8)

        rad1.place(x=20, y=520)
        rad2.place(x=80, y=520)
        rad3.place(x=850, y=240)
        rad4.place(x=850, y=280)
        visa_decLabel.place(x=850, y=340)
        rad5.place(x=850, y=370)
        rad6.place(x=850, y=400)
        visa_validLabel.place(x=850, y=440)
        rad7.place(x=850, y=470)
        rad8.place(x=850, y=500)

        Occ_label = Label(self, text="21. Current occupation: ")
        Occ_label.place(x=20, y=550)

        occ = Entry(self, width=25)
        occ.place(x=200, y=550)

        Emp_add_label = Label(self,
                              text="22. Employer and Employer's address and telephone number. For students; name and address of educational establishment: ")
        Emp_add_label.place(x=20, y=580)

        occ = Entry(self, width=60)
        occ.place(x=40, y=610)

        pur_label = Label(self, text="23. Purpose(s) of the journey: ")
        pur_label.place(x=20, y=640)

        rad1 = Radiobutton(self, text='Tourism', value=1)
        rad2 = Radiobutton(self, text='Business', value=2)
        rad3 = Radiobutton(self, text='Visiting family or friends', value=3)
        rad4 = Radiobutton(self, text='Cultural', value=4)
        rad5 = Radiobutton(self, text='Sports', value=5)
        rad6 = Radiobutton(self, text='Official visit', value=6)
        rad7 = Radiobutton(self, text='Medical reasons', value=7)
        rad8 = Radiobutton(self, text='Study', value=8)

        rad1.place(x=20, y=660)
        rad2.place(x=90, y=660)
        rad3.place(x=160, y=660)
        rad4.place(x=320, y=660)
        rad5.place(x=400, y=660)
        rad6.place(x=460, y=660)
        rad7.place(x=550, y=660)
        rad8.place(x=670, y=660)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1)).place(x=350, y=680)
        button2 = ttk.Button(self, text="Page3",
                             command=lambda: controller.show_frame(Page3)).place(x=450, y=680)

# CODE FOR PAGE 3


class Page3(tk.Frame):

    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)

        header = Label(self, text="Harmonised application form",
                       font=('bold', 14))
        header.place(x=400, y=20)
        title = Label(self, text="Application for Schengen Visa",
                      font=('bold', 14))
        title.place(x=400, y=50)
        subTitle = Label(self, text="This application form is free")
        subTitle.place(x=450, y=80)

        page_label = Label(self, text="page 3: ")
        page_label.place(x=920, y=30)

        add_info_label = Label(
            self, text="24. Additional information on purpose of stay: ")
        add_info_label.place(x=20, y=120)

        add_info = Entry(self, width=90)
        add_info.place(x=300, y=120)

        mem_state_label = Label(self,
                                text="25. Member State of main destination (and other \n     Member States of destination , if applicable): ")
        mem_state_label.place(x=20, y=150)

        mem_state = Entry(self, width=30)
        mem_state.place(x=300, y=150)

        mem_state2_label = Label(self, text='26. Member State of first entry:')
        mem_state2_label.place(x=500, y=150)

        mem_state = Entry(self, width=28)
        mem_state.place(x=673, y=150)

        num_entries_label = Label(
            self, text='27. Number of entries requested:')
        num_entries_label.place(x=20, y=190)

        rad1 = Radiobutton(self, text='Single entry', value=1)
        rad2 = Radiobutton(self, text='Two entries', value=2)
        rad3 = Radiobutton(self, text='Multiple entries', value=3)

        rad1.place(x=20, y=210)
        rad2.place(x=120, y=210)
        rad3.place(x=220, y=210)

        int_doa_label = Label(
            self, text='Intended date of arrival of the first intended stay in the Schengen area:')
        int_doa_label.place(x=340, y=190)

        arr_date = Entry(self, width=15)
        arr_date.place(x=750, y=190)

        num_entries_label = Label(self,
                                  text='Intended date of departure from the Schengen area after first intended stay:')
        num_entries_label.place(x=340, y=210)

        dep_date = Entry(self, width=15)
        dep_date.place(x=750, y=210)

        fingerprint_label = Label(self,
                                  text='28. Fingerprints collected previously for the purpose of applying for a Schengen visa:')
        fingerprint_label.place(x=20, y=240)

        rad1 = Radiobutton(self, text='Yes', value=1)
        rad2 = Radiobutton(self, text='No', value=2)

        rad1.place(x=480, y=240)
        rad2.place(x=530, y=240)

        fingerprint_label = Label(self,
                                  text='Date,  if known ........................................... Visa sticker number, if known   ............................................:')
        fingerprint_label.place(x=40, y=260)

        entry_per_label = Label(
            self, text='29. Entry permit for final country of destination, where applicable: ')
        entry_per_label.place(x=20, y=290)

        issuedby_label = Label(self,
                               text='Issued by  ........................................... Valid from ............................................ until .........................:')
        issuedby_label.place(x=40, y=310)

        surname_label = Label(self,
                              text='30. Surname and firstname of the inviting person(s) in the Member State(s). if not applicable, name of hotel(s) or temporary accommodation(s) in the Member State(s):')
        surname_label.place(x=20, y=340)

        surname = Entry(self, width=100)
        surname.place(x=40, y=360)

        entry_per_label = Label(self,
                                text=' Address and e-mail address of inviting person(s)/hotel(s)/temporary accomodation(s): ')
        entry_per_label.place(x=35, y=380)

        surname = Entry(self, width=60)
        surname.place(x=500, y=380)

        phone_label = Label(self, text=' Telephone no.: ')
        phone_label.place(x=35, y=400)

        surname = Entry(self, width=60)
        surname.place(x=500, y=400)

        name_add_label = Label(
            self, text='31. Name and address of inviting company/organisation: ')
        name_add_label.place(x=20, y=430)

        name = Entry(self, width=60)
        name.place(x=500, y=430)

        sur_name_label = Label(self,
                               text=' Surname, firstname, address, telephone no. and e-mail address of contact person in company/organisation: ')
        sur_name_label.place(x=35, y=460)

        surname = Entry(self, width=42)
        surname.place(x=610, y=460)

        phone_label = Label(
            self, text=' Telephone no. of company/organisation: ')
        phone_label.place(x=35, y=490)

        surname = Entry(self, width=60)
        surname.place(x=500, y=490)

        travel_cost_label = Label(self,
                                  text='32. Cost of travelling and living during the applicant''s stay is covered: ')
        travel_cost_label.place(x=20, y=520)

        name = Entry(self, width=60)
        name.place(x=500, y=520)

        rad1 = Radiobutton(
            self, text='by the applicant himself/herself', value=1)
        rad1.place(x=35, y=545)

        phone_label = Label(self, text=' Means of support: ')
        phone_label.place(x=35, y=565)

        rad1 = Radiobutton(self, text='Cash', value=1)
        rad2 = Radiobutton(self, text='Travellers cheques', value=2)
        rad3 = Radiobutton(self, text='Credit card', value=3)
        rad4 = Radiobutton(self, text='Pre-paid accomodation', value=4)

        rad1.place(x=35, y=590)
        rad2.place(x=100, y=590)
        rad3.place(x=230, y=590)
        rad4.place(x=330, y=590)

        button1 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2)).place(x=350, y=680)
        button2 = ttk.Button(self, text="Page4",
                             command=lambda: controller.show_frame(Page4)).place(x=450, y=680)

        # CODE FOR PAGE 3


class Page4(tk.Frame):

    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        # The headers and titles
        header = Label(self, text="Harmonised application form",
                       font=('bold', 14))
        header.place(x=400, y=20)
        title = Label(self, text="Application for Schengen Visa",
                      font=('bold', 14))
        title.place(x=400, y=50)
        subTitle = Label(self, text="This application form is free")
        subTitle.place(x=450, y=80)

        page_label = Label(self, text="page 4: ")
        page_label.place(x=920, y=30)

        rad5 = Radiobutton(self, text='Pre-paid transport', value=5)
        rad6 = Radiobutton(self, text='Other (please specify):', value=6)
        rad7 = Radiobutton(
            self, text='by a sponsor(host, company, organisation) please specify:', value=7)
        rad8 = Radiobutton(self,
                           text='..................................................... refered to in field 30 or 31 ...................................... other (please specify):',
                           value=8)

        rad5.place(x=30, y=120)
        rad6.place(x=160, y=120)
        rad7.place(x=35, y=150)
        rad8.place(x=35, y=180)

        others = Entry(self, width=60)
        others.place(x=500, y=120)

        specify = Entry(self, width=43)
        specify.place(x=600, y=180)

        other = Entry(self, width=60)
        other.place(x=500, y=150)

        phone_label = Label(self, text=' Means of support: ')
        phone_label.place(x=35, y=210)

        rad1 = Radiobutton(self, text='Cash', value=1)
        rad2 = Radiobutton(self, text='Accomodation provided', value=2)
        rad3 = Radiobutton(
            self, text='All expenses covered during the stay', value=3)
        rad4 = Radiobutton(self, text='Pre-paid transport', value=4)
        rad5 = Radiobutton(self, text='Other (please specify)', value=5)

        rad1.place(x=35, y=230)
        rad2.place(x=95, y=230)
        rad3.place(x=260, y=230)
        rad4.place(x=480, y=230)
        rad5.place(x=605, y=230)

        other = Entry(self, width=18)
        other.place(x=750, y=230)

        Button(self, text='Submit', width=20, bg='brown',
               fg='white').place(x=230, y=470)
        button1 = ttk.Button(self, text="Page 3",
                             command=lambda: controller.show_frame(Page3)).place(x=350, y=680)
        button2 = ttk.Button(self, text="Summary",
                             command=lambda: controller.show_frame(Summary)).place(x=450, y=680)

# SUMMARY PAGE


class Summary(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        label = ttk.Label(self, text="Summary", font=LARGEFONT)
        label.grid(row=0, column=4)

        Button(self, text='Submit', width=20, bg='brown',
               fg='white').place(x=230, y=470)
        button1 = ttk.Button(self, text="Page 4",
                             command=lambda: controller.show_frame(Page4)).place(x=350, y=680)
        button2 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(StartPage)).place(x=450, y=680)

    # Driver Code


app = tkinterApp()
app.geometry('1000x900+20+20')
app.title('Visa Application Form')
app.mainloop()
