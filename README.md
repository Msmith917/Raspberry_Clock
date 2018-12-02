# Raspberry_Clock
> Private repository dedicated to my raspberry pi smart clock project. 
> This project will be to create a smart clock for my room

### Functions (should include but not limited to):
  ##### - Reading indoor and outdoor temperature and humidity
  ##### - Give update on current weather
  ##### - Tell the current time
  ##### - Ability to talk to me, i.e. (JASPER: tell me time, remind me to do things)
  ##### - Do I need a jacket? 

*I will step by step by step work to incorporate each of these functions to the Raspberry Pi
even using the Arduino as well. Start with a simple program that runs and on an infinite
loop and will not fail.*

## 1. Read Indoor/Outdoor Temperature
> My goal with step one is to make a board that can read the temperature in my room and the temperature and humidity outside

- First I used a lm35 reciever connected to an Arduino UNO so that I could recieve and covert the temperature to a readable float

The following code is used on an Arduino UNO and compiled on my Raspberry Pi to grab the temperature, convert it, print out the degrees in fahrenheit to terminal
##### Code used for Arduino UNO
```C 
// initialize variables for the pin, and the floats, (celsius, and fahrenheit)
float temp;
int temp_pin = 2;
float temp_f;

void setup() {
  // begin the communication between devices
  Serial.begin(9600);
}

void loop() {
  // convert the volts to fahrenheit
  temp = analogRead(temp_pin);
  temp_f = temp * .48828125;
  temp_f = temp_f * 9/5;
  temp_f = temp_f + 32;
  // print the number to the serial monitor
  Serial.println(temp_f);
  delay(1000);
}
```
##### Code used for Raspberry written in Python3.6
```Python
import serial, re, os, time
from serial import Serial

while True:
  #Clear the *linux* terminal
  os.system('clear') 
  #Grab the serial read from Arduino UNO
  ser = serial.Serial('/dev/ttyACM0', 9600)
  #Read the updated line 
  byt = ser.readline()
  #Use a regex to convert the byte info into a float
  res = re.compile('\d+.\d+')
  temp = res.search(str(byt))
  temp_f = round(float(temp.group()))
  #Print the temperature in fahrenheit
  print(temp_f)
  #Pause the loop for 1 second
  time.sleep(1)
  ```
## 2. Weather Report
> Step 2 is creating a user interface that reads the current weather 

- Python comes with a weather-api, makes for reading the weather and displaying it appropriately easy

```Python
from weather import Weather, Unit
weather = Weather(unit=Unit.FAHRENHEIT)

location = weather.lookup_by_location('beaumont')
forecasts = location.forecast

def report(i):
  date = forecasts[i].date
  condition = forecasts[i].text
  high = forecasts[i].high
  low = forecasts[i].low
  
  print(f'Weather in Bmt, Texas {date}')
  print(f'{condition} with a high of: {high} and a low of: {low}')
  
report(0) #current day report
report(1) #report for tomorrow
```

## 3. The Clock
> Finally building the actual user interface for the clock; the most work will be put in here, but changes and additions should happen regularly

- Basic clock UI with Python's module tkinter

```Python
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
```

## Version: 0.1
> A very basic and simple outlook on where I am at.

Functions include:
  - Telling of time
  - Reading indoor temperature
  - Current date
  - Weather report for today and tomorrow
  
```Python
import tkinter, serial, re, os, time, weather
from serial import Serial
from tkinter import *
from weather import Weather, Unit

weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('beaumont')
forecasts = location.forecast

def tick():
	time_string = time.strftime("%I:%M %p")
	current_time.config(text=time_string)
	current_time.after(100,tick)

def today():
	condition = forecasts[0].text
	high = forecasts[0].high
	low = forecasts[0].low
	
	today_forecast.config(text=f'Weather for today in Bmt, Texas\n{condition} with a high of: {high} and a low of: {low}')
	#today_forecast.after(300000,today)
	
def tomorrow():
	condition = forecasts[1].text
	high = forecasts[1].high
	low = forecasts[1].low
	
	tomorrow_forecast.config(text=f'Weather for Tomorrow in Bmt, Texas\n{condition} with a high of: {high} and a low of: {low}')
	tomorrow_forecast.after(300000,tomorrow)

def roomTemp():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	byt = ser.readline()
	res = re.compile('\d+.\d+')
	temp = res.search(str(byt))
	temp_f = round(float(temp.group()))
	indoor_temp.config(text=f'Room Temperature: {temp_f}')
	indoor_temp.after(20000,roomTemp)
	
def date():
	date = forecasts[0].date
	current_date.config(text=date)
		
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

today()
tomorrow()
roomTemp()
date()
tick()
root.mainloop()
```
