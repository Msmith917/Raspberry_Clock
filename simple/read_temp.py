# Reads the Indoor Temperature
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
  temp = res.findall(str(byt))
  if len(temp) == 3:
    print(temp)
    inTemp = round(float(temp[0]))
    outTemp = round(float(temp[1]))
    hum = round(float(temp[2]))
  #Print the temperature in fahrenheit
    print(inTemp)
    print(outTemp)
    print(hum)
  else:
    pass
  #Pause the loop for 1 second
  time.sleep(1)
