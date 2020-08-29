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
        for F in (StartPage, Reg_page, Page1, Page2, Summary):
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
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.place(x=350, y=650)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="page1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button2.place(x=450, y=650)


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
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.place(x=350, y=650)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.place(x=450, y=650)

    # third window frame page2

# CODE FOR PAGE2(CONTINUATION OF PAGE 1 FORM)


class Page2(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.place(x=350, y=650)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Summary",
                             command=lambda: controller.show_frame(Summary))

        # putting the button in its place by
        # using grid
        button2.place(x=450, y=650)


# SUMMARY PAGE
class Summary(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        label = ttk.Label(self, text="Summary", font=LARGEFONT)
        label.grid(row=0, column=4)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button1.place(x=350, y=650)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.place(x=450, y=650)

    # Driver Code


app = tkinterApp()
app.geometry('1000x900+20+20')
app.title('Visa Application Form')
app.mainloop()
