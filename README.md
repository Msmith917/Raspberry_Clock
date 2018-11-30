# Raspberry_Clock
> Private repository dedicated to my raspberry pi smart clock project. 
> This project will be to create a smart clock for my room

### Functions (should include but not limited to):
  ##### - Reading indoor and outdoor temperature and humidity
  ##### - Give update on current weather
  ##### - Ability to talk to me, i.e. (tell me time, remind me to do things)
  ##### - Joke of the day button
  ##### - Smart Irrigation system, water plants and feed fish?

*I will step by step by step work to incorporate each of these functions to the Raspberry Pi
even using the Arduino as well. Start with a simple program that runs and on an infinite
loop and will not fail.*

## 1. Temperature Control
> My goal with step one is to create a useable thermostate that can read the temperature in my room

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
