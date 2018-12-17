from weather import Weather, Unit
import pyttsx3

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