# The very first version of my Pi_Clock
import tkinter, serial, re, os, time, weather
from serial import Serial
from tkinter import *
from weather import Weather, Unit

# Initialize the Weather API and set up the forecasts
weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('beaumont')
forecasts = location.forecast

# Tick function for the clock that will be displayed
def tick():
	time_string = time.strftime("%I:%M %p")
	current_time.config(text=time_string)
	# Allows the clock to be constantly updating in the screen
	current_time.after(100,tick)

# Sets up the forecast for today to be displayed
def today():
	condition = forecasts[0].text
	high = forecasts[0].high
	low = forecasts[0].low

	today_forecast.config(text=f'Weather for today in Bmt, Texas\n{condition} with a high of: {high} and a low of: {low}')
	# Allows the forcast to update every five minutes
	today_forecast.after(300000,today)

# Forecast function for the following day
def tomorrow():
	condition = forecasts[1].text
	high = forecasts[1].high
	low = forecasts[1].low

	tomorrow_forecast.config(text=f'Weather for Tomorrow in Bmt, Texas\n{condition} with a high of: {high} and a low of: {low}')
	# Display updates every five minutes
	tomorrow_forecast.after(300000,tomorrow)

# Uses the Arduino to find the Serial Number and read the indoor temperature
def roomTemp():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	byt = ser.readline()
	# Uses a regex to pull a string from the byte format type
	res = re.compile('\d+.\d+')
	temp = res.search(str(byt))
	temp_f = round(float(temp.group()))
	indoor_temp.config(text=f'Room Temperature: {temp_f}')
	indoor_temp.after(20000,roomTemp)

# Sets the current date on the using the weather-API
def date():
	date = forecasts[0].date
	current_date.config(text=date)

# The Final Build for the User Interface
root = tkinter.Tk()
root.title('Pi_Clock')
root.geometry("750x200")
current_date = Label(root, text="Today's Date")
today_forecast = Label(root, text="Today's Forecast")
tomorrow_forecast = Label(root, text="Tomorrow's Forecast")
current_time = Label(root, text='Current Time', font=('times', 60))
indoor_temp = Label(root, text='Indoor Temp')

current_date.place(x=350, y=20)
today_forecast.place(x=20, y=40 )
tomorrow_forecast.place(x=20, y=100)
current_time.place(x=400, y=80)
indoor_temp.place(x=500, y=20)

# Run all the function 
today()
tomorrow()
roomTemp()
date()
tick()
root.mainloop()
