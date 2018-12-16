import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Pi_Clock')
current_date = Label(root, text="Today's Date")
today_forecast = Label(root, text="Today's Forecast")
tomorrow_forecast = Label(root, text="Tomorrow's Forecast")
current_time = Label(root, text='Current Time', font=('times', 60))
indoor_temp = Label(root, text='Indoor Temp')
outdoor_temp = Label(root, text='Outdoor Temp')
humidity = Label(root, text='Humidity')

def new_winF(): # new window definition
    newwin = Toplevel(root)
    display = Label(newwin, text="Humm, see a new window !")
    display.pack()

button1 =Button(root, text ="open new window", command =new_winF) #command linked

indoor_temp.pack(side='left', side='top')
outdoor_temp.pack(side='right', side='top')
button1.pack()

current_date.pack()
today_forecast.pack()
tomorrow_forecast.pack()
current_time.pack()


humidity.pack()

root.mainloop()
