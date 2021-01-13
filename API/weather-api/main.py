#!/usr/bin/env python3


import requests, json 
import os
import datetime
import pyfiglet



result = pyfiglet.figlet_format("Weather API")
print(result)
print("\n") # describtion-row
os.system("date")
print("-------------------------------------")




#ENTER YOUR API KEY

api_key = "" 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ") 

complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 

x = response.json() 

if x["cod"] != "404": 

	y = x["main"] 

	current_temperature = y["temp"] 
	current_pressure = y["pressure"] 
	current_humidiy = y["humidity"] 

	z = x["weather"] 

	weather_description = z[0]["description"] 

	# print following values 
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

else: 
	print(" Fail ") 

