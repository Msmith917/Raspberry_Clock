#include <Adafruit_Sensor.h>
#include <DHT.h>
#define dht_pin 2
#define DHTTYPE DHT22

// initialize variables for the pin, and the floats, (celsius, and fahrenheit)
float temp;
int temp_pin = 2;
float temp_f;

DHT dht(dht_pin, DHTTYPE);

void setup() {
  // begin the communication between devices
  Serial.begin(9600);
}

void loop() {
  temp = analogRead(temp_pin);
  temp_f = temp * .48828125;
  temp_f = temp_f * 9/5;
  temp_f = temp_f + 32;
  Serial.print(temp_f);
  Serial.print(" ");
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  t = t * 9/5;
  t = t + 32;
  Serial.print(t);
  Serial.print(" ");
  Serial.print(h);
  Serial.println("");
  delay(1000);
}
// Prints xx.x yy.y zz.z
