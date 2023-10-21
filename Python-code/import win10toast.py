from tkinter import *
from tkcalendar import *

ws = Tk()
ws.title("Python Guides")
ws.geometry("500x400")
ws.config(bg="#cd950c")

hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""        
f = ('Times', 20)

def display_msg():
    date = cal.get_date()
    return date
       


if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)   
    last_value = min_string.get()

if last_value_sec == "59" and sec_hour.get() == "0":
    min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
if last_value == "59":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)            
    last_value_sec = sec_hour.get()

fone = Frame(ws)
ftwo = Frame(ws)

fone.pack(pady=10)
ftwo.pack(pady=10)

cal = Calendar(
    fone, 
    selectmode="day", 
    year=2023, 
    month=10,
    day=30
    )
cal.pack()


actionBtn =Button(
    ws,
    text="Book Appointment",
    padx=10,
    pady=10,
    string=display_msg
    print(string)
)
actionBtn.pack(pady=10)

msg_display = Label(
    ws,
    text="",
    bg="#cd950c"
)
msg_display.pack(pady=10)

ws.mainloop()