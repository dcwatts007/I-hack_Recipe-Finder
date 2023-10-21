import tkinter
from tkinter import *
window = Tk()

# text labels
label = Label(window, text="Welcome to the bodacious bohemoths app", fg='black', font=("Helvetica", 20))
label.place(x=90, y=50)

label = Label(window, text="Please input your ingredients", fg='black', font=("Helvetica", 16))
label.place(x=90, y=125)

label = Label(window, text="(Click button when finished)", fg='black', font=("Helvetica", 12))
label.place(x=90, y=150)

# window frame and title
window.title("Hello there!")
window.geometry("900x600+300+50")
window.mainloop()