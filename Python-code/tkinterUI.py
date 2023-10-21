from tkinter import *
from tkinter.ttk import Combobox
window = Tk()

# text labels
label1 = Label(window, text="Welcome to the bodacious bohemoths app", fg='black', font=("Helvetica", 20, "bold"))
label1.place(x=90, y=10)

label2 = Label(window, text="Please input your ingredients:", fg='black', font=("Helvetica", 16))
label2.place(x=90, y=50)

label3 = Label(window, text="(Check the checkbox when finished)", fg='black', font=("Helvetica", 12))
label3.place(x=90, y=80)

label4 = Label(window, text="INGREDIENT", fg='black', font=("Helvetica", 12))
label4.place(x=105, y=125)

label5 = Label(window, text="EXP DATE", fg='black', font=("Helvetica", 12))
label5.place(x=260, y=125)

label6 = Label(window, text="INGREDIENT", fg='black', font=("Helvetica", 12))
label6.place(x=446, y=125)

label6 = Label(window, text="EXP DATE", fg='black', font=("Helvetica", 12))
label6.place(x=600, y=125)

# text box entry
tb1 = Entry(window, bd=5)
tb1.place(x=90, y=150)
tbd1 = Entry(window, bd=5)
tbd1.place(x=235, y=150)

tb2 = Entry(window, bd=5)
tb2.place(x=90, y=185)
tbd2 = Entry(window, bd=5)
tbd2.place(x=235, y=185)

tb3 = Entry(window, bd=5)
tb3.place(x=90, y=220)
tbd3 = Entry(window, bd=5)
tbd3.place(x=235, y=220)

tb4 = Entry(window, bd=5)
tb4.place(x=90, y=255)
tbd4 = Entry(window, bd=5)
tbd4.place(x=235, y=255)

tb5 = Entry(window, bd=5)
tb5.place(x=90, y=290)
tbd5 = Entry(window, bd=5)
tbd5.place(x=235, y=290)

tb6 = Entry(window, bd=5)
tb6.place(x=90, y=325)
tbd6 = Entry(window, bd=5)
tbd6.place(x=235, y=325)

tb7 = Entry(window, bd=5)
tb7.place(x=90, y=360)
tbd7 = Entry(window, bd=5)
tbd7.place(x=235, y=360)

tb8 = Entry(window, bd=5)
tb8.place(x=90, y=395)
tbd8 = Entry(window, bd=5)
tbd8.place(x=235, y=395)

tb9 = Entry(window, bd=5)
tb9.place(x=90, y=430)
tbd9 = Entry(window, bd=5)
tbd9.place(x=235, y=430)

tb10 = Entry(window, bd=5)
tb10.place(x=90, y=465)
tbd10 = Entry(window, bd=5)
tbd10.place(x=235, y=465)

tb11 = Entry(window, bd=5)
tb11.place(x=430, y=150)
tbd11 = Entry(window, bd=5)
tbd11.place(x=575, y=150)

tb12 = Entry(window, bd=5)
tb12.place(x=430, y=185)
tbd12 = Entry(window, bd=5)
tbd12.place(x=575, y=185)

tb13 = Entry(window, bd=5)
tb13.place(x=430, y=220)
tbd13 = Entry(window, bd=5)
tbd13.place(x=575, y=220)

tb14 = Entry(window, bd=5)
tb14.place(x=430, y=255)
tbd14 = Entry(window, bd=5)
tbd14.place(x=575, y=255)

tb15 = Entry(window, bd=5)
tb15.place(x=430, y=290)
tbd15 = Entry(window, bd=5)
tbd15.place(x=575, y=290)

tb16 = Entry(window, bd=5)
tb16.place(x=430, y=325)
tbd16 = Entry(window, bd=5)
tbd16.place(x=575, y=325)

tb17 = Entry(window, bd=5)
tb17.place(x=430, y=360)
tbd17 = Entry(window, bd=5)
tbd17.place(x=575, y=360)

tb18 = Entry(window, bd=5)
tb18.place(x=430, y=395)
tbd18 = Entry(window, bd=5)
tbd18.place(x=575, y=395)

tb19 = Entry(window, bd=5)
tb19.place(x=430, y=430)
tbd19 = Entry(window, bd=5)
tbd19.place(x=575, y=430)

tb20 = Entry(window, bd=5)
tb20.place(x=430, y=465)
tbd20 = Entry(window, bd=5)
tbd20.place(x=575, y=465)

# check mark
data = ("one", "two", "three", "four")
v1 = IntVar()
def check_checkbox():
    if v1.get() == 1:
        cblabel.place(x=760, y=200)
        cb.place(x=790, y=260)
    elif v1.get() == 0:
        cblabel.place(x=-400, y=-200)
        cb.place(x=-200, y=-200)
cblabel= Label(window, text="Please select display option:", fg='black', font=("Helvetica", 20))
cb = Combobox(window, values=data, state="readonly", height= 5 ,font="Verdana 16")
C1 = Checkbutton(window, text="Check here when finished", onvalue= 1, offvalue= 0, 
                 variable= v1, command= check_checkbox)
C1.place(x=800, y=500)




# window frame and title
window.title("Hello there!")
window.geometry("1200x600+150+50")
window.mainloop()