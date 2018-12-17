import tkinter
from tkinter import *

def new_winF(): # new window definition

    newwin = Toplevel(root)
    # widgits used in the new window frame
    today_forecast = Label(newwin, text="Today's Forecast")
    tomorrow_forecast = Label(newwin, text="Tomorrow's Forecast")
    humidity = Label(newwin, text='Humidity')
    outdoor_temp = Label(newwin, text='Outdoor Temp')

    today_forecast.pack()
    tomorrow_forecast.pack()
    outdoor_temp.pack()
    humidity.pack()

# main window for the application
root = tkinter.Tk()
root.title('Pi_Clock')

# Widgets used in application
current_date = Label(root, text="Today's Date")
current_time = Label(root, text='Current Time', font=('times', 60))
indoor_temp = Label(root, text='Indoor Temp')
outdoor_temp = Button(root, text='Outdoor Temp', command=new_winF)
jacket = Button(root, text='Do I Need A Jacket?')


# the pack and griding for all the widgets 
indoor_temp.pack(side='left', padx=30, pady=30)
outdoor_temp.pack(side='right', padx=30, pady=30)

current_date.pack(side='top', padx=30, pady=30)
current_time.pack(anchor='center', padx=30, pady=100)

jacket.pack(side='bottom', pady=100)

root.mainloop()
