import time 
import Adafruit_DHT

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

sensor = Adafruit_DHT.DHT11
pin = 4

payload = {}

def read():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    try:
        if humidity is not None and temperature is not None:
            payload = {
                'timestamp': str(time.time()),
                'temperature': str(temperature),
                'humidity': str(humidity)
            }
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        log.error("Reading from DHT failure: " + e.args)    
    return payload

'''
while True:
    try:
        if humidity is not None and temperature is not None:
            print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
 
    time.sleep(5)
'''