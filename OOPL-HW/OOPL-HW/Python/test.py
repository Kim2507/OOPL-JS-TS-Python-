import requests
import json
url ='https://wttr.in/Boston?format=j1'

#print(f"Getting live data from {url}")

r = requests.get(url)
weather_report=  r.json()

# Getting feel like temp info 
#print(f"Sunset: {weather_report['weather'][0]['astronomy'][0]['sunset']}")
#feel_like = [0][0][2]
#print(json.load(weather_report))
#feel_like = weather_report['current_condition'][0]['FeelsLikeF']
#cloud_cover = weather_report['current_condition'][0]['cloudcover']
#weather_description = weather_report['current_condition'][0]['weatherDesc'][0]['value']
#sunset = weather_report['weather'][0]['astronomy'][0]['sunset']
#sunrise = weather_report['weather'][0]['astronomy'][0]['sunrise']
#print(f"Feels Like: {feel_like}\nCloud Cover: {cloud_cover}\nWeather Description: {weather_description}\
	#\nSunset:{sunset}\nSunrise:{sunrise}")

