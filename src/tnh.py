import time 
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

while True:
    try:
        if humidity is not None and temperature is not None:
            print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
 
    time.sleep(5)