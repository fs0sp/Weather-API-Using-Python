import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b149867edf3c9f3df9709b22b7ad882a&q='

city = input('Enter the City Name : ')

url = api_address + city

json_data = requests.get(url).json()


min_temp = json_data['main']['temp_min']
max_temp = json_data['main']['temp_max']
current_temp = json_data['main']['temp']
description = json_data['weather'][0]['description']

celsius = current_temp - 273
	

print("The Current Temperature of {} is : {:.2f} Degree ".format(city,celsius))
print("Maximum Temp : {} , Minimum Temp : {}".format(min_temp,max_temp))
print("Description : {}  ".format(description))