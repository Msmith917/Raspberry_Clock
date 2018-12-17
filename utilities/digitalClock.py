# This is the Code for a simple Digital Clock UIs
import time, tkinter
from tkinter import *

def tick():
    time_string = time.strftime("%I:%M:%S %p")
    clock.config(text=time_string)
    clock.after(200,tick)

root = tkinter.Tk()
clock = Label(root, font=('times', 200))
clock.grid(row=0, column=1)
tick()

root.mainloop()