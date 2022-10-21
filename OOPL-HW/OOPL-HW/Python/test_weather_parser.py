import unittest
#import requests
#import weather_parser
from weather_parser import *
#import weather_parser

class TestWeatherParser(unittest.TestCase):
	"""Test for weather_parser.py"""
	#url ="https://wttr.in/Boston?format=j1"

	#r = requests.get(url)
	#read_weather=  r.json()
	#weather_parser.read_weather = weather_report

	def test_get_feels_like(self):
		feels_like = get_feels_like_f()
		assertIn(feels_like,range(0,100))

	#def test_get_cloud_cover(self):
		#cloud_cover = get_cloud_cover()
		#assertNotEqual(cloud_cover,'None')

	#def test_get_weather_description(self):
		#weather_desc  = get_weather_description()
		#assertNotEqual(weather_desc,'None')


	#def test_get_sunset(self):
		#sunset = get_sunset()
		#assertNotEqual(sunset,'None')


	#def test_get_sunrise(self):
		#sunrise = get_sunrise()
		#assertNotEqual(get_sunset(),'None')

if __name__ == '__main__':
	unittest.main()
