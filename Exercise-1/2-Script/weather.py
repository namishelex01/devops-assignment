#!/usr/bin/env python3

import os
import sys
import pyowm

try:
    api_key = os.environ['OWM_API_KEY']
    city = os.environ['OWM_CITY']
except Exception as e:
    print(e)
    sys.exit(1)

def run(api_key, city):
    try:
        owm = pyowm.OWM(api_key)
        report = owm.weather_manager().weather_at_place(city).weather
        result = "City='{cityname}', Description='{description}', Temperature(in Celsius)={temp}, Humidity={hum}".format(
            cityname=city,
            description=str(report.detailed_status),
            temp=str(report.temperature('celsius')['temp']),
            hum=str(report.humidity)
        )
        print(result)
    except Exception as e:
        print(e)
        sys.exit(0)

run(api_key, city)