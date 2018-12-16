import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Pi_Clock')
root.geometry("750x200")
current_date = Label(root, text="Today's Date")
today_forecast = Label(root, text="Today's Forecast")
tomorrow_forecast = Label(root, text="Tomorrow's Forecast")
current_time = Label(root, text='Current Time', font=('times', 60))
indoor_temp = Label(root, text='Indoor Temp')
outdoor_temp = Label(root, text='Outdoor Temp')
humidity = Label(root, text='Humidity')

current_date.place(x=350, y=20)
today_forecast.place(x=20, y=40 )
tomorrow_forecast.place(x=20, y=100)
current_time.place(x=20, y=150)
indoor_temp.place(x=300, y=40)
outdoor_temp.place(x=300, y=60)
humidity.place(x=350, y=80)

root.mainloop()