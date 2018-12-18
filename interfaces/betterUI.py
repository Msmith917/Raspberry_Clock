import tkinter
from tkinter import *

def new_winF(): # new window definition

    newwin = Toplevel(root)
    newwin.configure(background='#060614')
    # widgits used in the new window frame
    today_forecast = Label(newwin, text="Today's Forecast", bg='#060614', fg='#cccccc')
    tomorrow_forecast = Label(newwin, text="Tomorrow's Forecast", bg='#060614', fg='#cccccc')
    humidity = Label(newwin, text='Humidity', bg='#060614', fg='#cccccc')
    outdoor_temp = Label(newwin, text='Outdoor Temp', bg='#060614', fg='#cccccc')

    today_forecast.pack()
    tomorrow_forecast.pack()
    outdoor_temp.pack()
    humidity.pack()

# main window for the application
root = tkinter.Tk()
root.title('Pi_Clock')
root.configure(background='#060614')

# Widgets used in application
current_date = Label(root, text="Today's Date", bg='#060614', fg='#cccccc')
current_time = Label(root, text='Current Time', font=('times', 60), bg='#060614', fg='#cccccc')
indoor_temp = Label(root, text='Indoor Temp', bg='#060614', fg='#cccccc')
outdoor_temp = Button(root, text='Outdoor Temp', command=new_winF, bg='#060614', fg='#cccccc')
jacket = Button(root, text='Do I Need A Jacket?', bg='#060614', fg='#cccccc')


# the pack and griding for all the widgets 
indoor_temp.pack(side='left', padx=30, pady=30)
outdoor_temp.pack(side='right', padx=30, pady=30)

current_date.pack(side='top', padx=30, pady=30)
current_time.pack(anchor='center', padx=30, pady=100)

jacket.pack(side='bottom', pady=100)

root.mainloop()
