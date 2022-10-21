"""First version was using request to get live url
But here is secodn version which read local json file"""

import unittest
#import requests
import json

import weather_parser
from weather_parser import *
#weather_boston = WeatherParser("https://wttr.in/Boston?format=j1")
#reader = weather_boston.get_json_object(requests)

#Read a local json file by json.load()
filename='boston_weather.json'
try:
	with open(filename) as f:
		data = json.load(f)
except FileNotFoundError:
	print("File not found, please check again")
else:
	weather_boston = WeatherParser()
	#print(weather_boston.get_feels_like_f(data))


class TestWeatherParser(unittest.TestCase):
	#Test for weather_parser.py

	def test_get_feels_like(self):

		feels_like = weather_boston.get_feels_like_f(data)
		self.assertNotEqual(feels_like,'None')

	def test_get_cloud_cover(self):
		cloud_cover = weather_boston.get_cloud_cover(data)
		self.assertNotEqual(cloud_cover,'None')

	def test_get_weather_description(self):
		weather_desc= weather_boston.get_weather_description(data)
		self.assertNotEqual(weather_desc,'None')


	def test_get_sunset(self):
		sunset = weather_boston.get_sunset(data)
		self.assertNotEqual(sunset,'None')


	def test_get_sunrise(self):
		sunrise = weather_boston.get_sunrise(data)
		self.assertNotEqual(sunrise,'None')

if __name__ == '__main__':
	unittest.main()
