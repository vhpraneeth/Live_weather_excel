#!/usr/bin/env python3
import time
import requests
import pandas as pd

print('Process started')
df = pd.read_excel('Sheet.xlsx')
main_url = 'http://api.openweathermap.org/data/2.5/weather?appid=<api-key-here>&q={}'

while 1:  # repeat continuously
    new_df = []
    for row in df.values:
        if row[-1]:  # if Update is 1
            city = row[0]
            unit = row[3]
            url = main_url.format(city)
            data = requests.get(url).json()
            temp = data['main']['temp'] - 273.15  # temperature in C
            if 'F' in unit:
                temp = (temp * 1.8) + 32  # to F
            temp = '{:.1f}'.format(temp)
            row[1] = temp
            row[2] = data['main']['humidity']
        new_df.append(row)
    new_df = pd.DataFrame(new_df, columns=df.keys())
    new_df.to_excel('Sheet.xlsx', index=False)
    new_df.to_csv('Sheet.csv', index=False)
    time.sleep(1)
