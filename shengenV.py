from tkinter import *

root = Tk()
root.title('Visa Application Form')

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

sur_label = Label(root, text='1. Surname (Family Name): ')
sur_label.place(x=20, y=180)
surname = Entry(root, width=120)
surname.place(x=20, y=200)

sur_label2 = Label(root, text='2. Surname at birth (Former family name(s)): ')
sur_label2.place(x=20, y=230)
surname2 = Entry(root, width=120)
surname2.place(x=20, y=250)


root.mainloop()
