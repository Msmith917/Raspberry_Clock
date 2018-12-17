import tkinter, serial, re, os, time, weather, pyttsx3
from tkinter import *
from serial import Serial
from weather import Weather, Unit

# Initialize the Weather API and set up the forecasts
weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('beaumont')
forecasts = location.forecast

# Function for the command 'Do I need a jacket?'
def jacket():
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)

    def wearJacket():
        engine.say('You might want to wear a jacket')
        engine.runAndWait()

    def noJacket():
        engine.say('You probably will not need a jacket')
        engine.runAndWait()

    weather = Weather(unit=Unit.FAHRENHEIT)
    location = weather.lookup_by_location('beaumont')
    forecasts = location.forecast

    condition = forecasts[0].text
    low = int(forecasts[0].low)
    high = int(forecasts[0].high)

    if low < 50:
        wearJacket()
        pass

    elif high < 65:
        wearJacket()
        pass

    elif "Rainy" or "Rain" or "Raining" in condition:
        wearJacket()
        pass

    elif "Thunderstorm" or "Snow" or "Snowing" in condition:
        wearJacket()
        pass

    else:
        noJacket()

# Tick function for the clock that will be displayed
def tick():
	time_string = time.strftime("%I:%M %p")
	current_time.config(text=time_string)
	# Allows the clock to be constantly updating in the screen
	current_time.after(100,tick)

# Sets up the forecast for today to be displayed
def today(today_forecast):
	condition = forecasts[0].text
	high = forecasts[0].high
	low = forecasts[0].low

	today_forecast.config(text='Weather for today in Bmt, Texas\n{} with a high of: {} and a low of: {}'.format(condition, high, low))

# Forecast function for the following day
def tomorrow(tomorrow_forecast):
	condition = forecasts[1].text
	high = forecasts[1].high
	low = forecasts[1].low

	tomorrow_forecast.config(text='Weather for Tomorrow in Bmt, Texas\n{} with a high of: {} and a low of: {}'.format(condition, high, low))

# Uses the Arduino to find the Serial Number and read the indoor temperature
def Temperature():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	byt = ser.readline()
	# Uses a regex to pull a string from the byte format type
	res = re.compile('\d+.\d+')
	temp = res.findall(str(byt))
	if len(temp) == 3:
		inTemp = round(float(temp[0]))
		outTemp = round(float(temp[1]))
		hum = round(float(temp[2]))
		indoor_temp.config(text='Room Temperature: {}'.format(inTemp))
		outdoor_temp.config(text='Outdoor Temperature: {}'.format(outTemp))
		humidity.config(text='Humidity: {}'.format(hum))
		humidity.after(200, Temperature)
	else:
		Temperature()
	
	


# Sets the current date on the using the weather-API
def date():
	date = forecasts[0].date
	current_date.config(text=date)





""" This is the User Interface made with TKINTER """

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

    today(today_forecast)
    tomorrow(tomorrow_forecast)

# main window for the application
root = tkinter.Tk()
root.title('Pi_Clock')
root.configure(background='#060614')

# Widgets used in application
current_date = Label(root, text="Today's Date", bg='#060614', fg='#cccccc')
current_time = Label(root, text='Current Time', font=('times', 60), bg='#060614', fg='#cccccc')
indoor_temp = Label(root, text='Indoor Temp', bg='#060614', fg='#cccccc')
outdoor_temp = Button(root, text='Outdoor Temp', command=new_winF, bg='#060614', fg='#cccccc')
jacket = Button(root, text='Do I Need A Jacket?', bg='#060614', fg='#cccccc', command=jacket)


# the pack and griding for all the widgets 
indoor_temp.pack(side='left', padx=30, pady=30)
outdoor_temp.pack(side='right', padx=30, pady=30)

current_date.pack(side='top', padx=30, pady=30)
current_time.pack(anchor='center', padx=30, pady=100)

jacket.pack(side='bottom', pady=100)

date()
tick()

root.mainloop()