# Raspberry_Home
> Private repository dedicated to my raspberry pi smart home project. 
> This project will be to create a smart home for my room

### Functions (should include but not limited to):
  ##### - Reading/Adjusting temperature
  ##### - Motion sensor lights for when I walk in and out of a room
  ##### - Joke of the day button
  ##### - Record and send message when door is open during the day while I would be at school
  ##### - Smart Irrigation system, water plants and feed fish?

*I will step by step by step work to incorporate each of these functions to the Raspberry Pi
even using the Arduino as well. Start with a simple program that runs and on an infinite
loop and will not fail.*

## 1. Temperature Control
> My goal with step one is to create a useable thermostate that can read the temperature and control a fan 
> to adjust the temperature accordingly. So basically create an a/c unit and thermostate. 

- First I used a lm35 reciever connected to an Arduino UNO so that I could recieve and covert the temperature to a readable float
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
}```
