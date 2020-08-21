#!/usr/bin/env python3

import requests



url = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q={}"
city = "vijayawada"
url = url.format(city)
json_data = requests.get(url).json()           # get weather
formatted_data = json_data['weather'][0]['main'].lower()
tmp = int(json_data["main"]["temp"] - 273.15)

