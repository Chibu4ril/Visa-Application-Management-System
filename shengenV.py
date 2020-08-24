from tkinter import *

# the window setting
root = Tk()
root.geometry('1000x900+20+20')
root.title('Visa Application Form')


# The headers and titles
header = Label(root, text="Harmonised application form", font=('bold', 14))
header.place(x=20, y=20)
title = Label(root, text="Application for Schengen Visa",
              font=('bold', 14))
title.place(x=20, y=50)
subTitle = Label(root, text="This application form is free")
subTitle.place(x=20, y=80)

var = StringVar()
desc = Message(root, textvariable=var, width=800)

var.set("Family members of EU, EEA, CH citizens shall not fill in fields no. 21, 22, 30, 31 and 32 marked with *. \nFields 1-3 shall be filled in in accordance with the data in the travel document")
desc.place(x=20, y=130)

# The form
sur_label = Label(root, text='1. Surname (Family Name): ')
sur_label.place(x=20, y=180)
surname = Entry(root, width=120)
surname.place(x=20, y=200)

sur_label2 = Label(root, text='2. Surname at birth (Former family name(s)): ')
sur_label2.place(x=20, y=230)
surname2 = Entry(root, width=120)
surname2.place(x=20, y=250)

fname_label = Label(root, text='3. First name(s) (Given name(s)): ')
fname_label.place(x=20, y=280)
fname = Entry(root, width=120)
fname.place(x=20, y=300)

official = Label(root, text='FOR OFFICIAL USE ONLY',
                 font=('Helvetica', 9, 'bold'))
official.place(x=800, y=195)
doa_label = Label(root, text="Date of application: ")
doa_label.place(x=800, y=220)
doa_input = Entry(root, width=30)
doa_input.place(x=800, y=250)

app_numLabel = Label(root, text="Application number: ")
app_numLabel.place(x=800, y=275)
app_num = Entry(root, width=30)
app_num.place(x=800, y=300)

# date of birth( can be mordified)

dob_label = Label(root, text="4. Date of birth(day-month-year): ")
dob_label.place(x=20, y=330)
dob = Entry(root, width=30)
dob.place(x=20, y=350)

pob_label = Label(root, text="5. Place of birth: ")
pob_label.place(x=250, y=330)
pob = Entry(root, width=35)
pob.place(x=250, y=350)


cob_label = Label(root, text="6. Country of birth: ")
cob_label.place(x=250, y=380)
cob = Entry(root, width=35)
cob.place(x=250, y=400)


cn_label = Label(root, text="7. Current nationality: ")
cn_label.place(x=500, y=330)
cn = Entry(root, width=35)
cn.place(x=500, y=350)

nab_label = Label(root, text=" Nationality at birth if different : ")
nab_label.place(x=500, y=380)
nab = Entry(root, width=35)
nab.place(x=500, y=400)

cn_label = Label(root, text=" Other nationality: ")
cn_label.place(x=500, y=430)
cn = Entry(root, width=35)
cn.place(x=500, y=450)


selected = IntVar()

rad_label = Label(root, text=" 8. Gender: ")
rad1 = Radiobutton(root, text='Male', value=1, variable=selected)

rad2 = Radiobutton(root, text='Female', value=2, variable=selected)


rad_label.place(x=20, y=480)

rad1.place(x=20, y=500)

rad2.place(x=100, y=500)

parental_aut_label = Label(
    root, text=" parental authority(in case of minors)/legal guardian(surname, first name, address, if different \n from applicant's, telephoneno., e-mail address, and nationality): ")
parental_aut_label.place(x=20, y=600)
parental_aut = Entry(root, width=120)
parental_aut.place(x=20, y=650)
parental_aut2 = Entry(root, width=120)
parental_aut2.place(x=20, y=680)


root.mainloop()
