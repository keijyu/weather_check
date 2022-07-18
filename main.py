#APIリクエストに必要なライブラリ

import requests

url = 'https://weather.tsukumijima.net/api/forecast/city/080010'

tenki_data = requests.get(url).json()
tenki_data_description = tenki_data['description']
tenki_data_forecasts = tenki_data['forecasts']

#print(tenki_data)
print(tenki_data['title'])
print(' ')
print(tenki_data_description['publicTime'])
print(tenki_data_forecasts[0]['dateLabel'])
print(tenki_data_forecasts[0]['telop'])
print(tenki_data_forecasts[0]['temperature']['min']['celsius'])
print(tenki_data_forecasts[0]['temperature']['max']['celsius'])
print(' ')
print(tenki_data_forecasts[1]['dateLabel'])
print(tenki_data_forecasts[1]['telop'])
print(tenki_data_forecasts[1]['temperature']['min']['celsius'])
print(tenki_data_forecasts[1]['temperature']['max']['celsius'])
print(' ')
print(tenki_data_forecasts[2]['dateLabel'])
print(tenki_data_forecasts[2]['telop'])
print(tenki_data_forecasts[2]['temperature']['min']['celsius'])
print(tenki_data_forecasts[2]['temperature']['max']['celsius'])