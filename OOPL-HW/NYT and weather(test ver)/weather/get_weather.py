"""Progmmmer: My Kim Trinh
Last update: 10/16/2021"""
import requests
from weather_parser import *


answer =  input("Enter city: ")
url = "https://wttr.in/"+answer+"?format=j1"
weather_city = WeatherParser(url)
weather_reader = weather_city.get_json_object(requests)

#print current temperture feel like
print(f"Currently feels like: {weather_city.get_feels_like_f(weather_reader)} degrees F")
# print current weather condition
print(f"Current weather is: {weather_city.get_weather_description(weather_reader)}")
#print current cloud cover
print(f"Cloud Cover:{weather_city.get_cloud_cover(weather_reader)}%")
#print sunrise
print(f"Sunrise: {weather_city.get_sunrise(weather_reader)}")
#print sunset
print(f"Sunset: {weather_city.get_sunset(weather_reader)}")

