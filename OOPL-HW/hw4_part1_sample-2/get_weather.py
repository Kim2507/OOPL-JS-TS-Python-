# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 02:09:01 2021

@author: BUBU
"""

from weather_parser import*
import requests



city=input("Enter city: ")

url=f"https://wttr.in/{city}?format=j1"
#print(url)

r=requests.get(url)
print(r.headers['content-type'])

#print(r.text)
weather_report=r.text

city_weather=WeatherParser(weather_report)
print(f"Currently feels like: {city_weather.get_feels_like_f()} degrees F")
print(f"Current weather is:{city_weather.get_weather_description()}")
print(f"Cloud Cover:{city_weather.get_cloud_cover()}%")
print(f"Sunrise:{city_weather.get_sunrise()} AM")
print(f"Sunset:{city_weather.get_sunset()} PM")
