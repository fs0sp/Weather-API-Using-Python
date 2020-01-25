import requests
import os

api_key = os.environ.get('WEATHER_KEY')
add = '&q='

api_add = 'http://api.openweathermap.org/data/2.5/weather?appid=' + str(api_key) + add

city = input('Enter the City Name : ')

url = api_add + city

json_data = requests.get(url).json()

#print(url)

min_temp = json_data['main']['temp_min']
max_temp = json_data['main']['temp_max']
current_temp = json_data['main']['temp']
description = json_data['weather'][0]['description']

celsius = current_temp - 273
	

print("The Current Temperature of {} is : {:.2f} Degree ".format(city,celsius))
print("Maximum Temp : {} , Minimum Temp : {}".format(min_temp,max_temp))
print("Description : {}  ".format(description))