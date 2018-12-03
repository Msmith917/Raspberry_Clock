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