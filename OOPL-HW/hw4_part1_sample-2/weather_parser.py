# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 00:59:26 2021

@author: BUBU
"""
import json

class WeatherParser:
    
    def __init__(self, json_string):
        self.weather_report=json.loads(json_string)
        self.current=self.weather_report['current_condition'][0]
        self.sunrise=self.weather_report['weather'][0]['astronomy'][0]['sunrise']
        self.sunset=self.weather_report['weather'][0]['astronomy'][0]['sunset']
        #self.current=self.weather_report['places'][0]
        #self.sunrise=self.weather_report['places'][1]['post code']
        #self.sunset=self.weather_report['places'][1]['latitude']
        
        
    
    def get_feels_like_f(self):
        
        #return self.current['place name']
        return self.current['FeelsLikeF']
    
    
    def get_cloud_cover(self):
        
        return self.current['cloudcover']
    
    
    def get_weather_description(self):
        
        #return self.current['post code']
        return self.current['weatherDesc'][0]['value']
    
    def get_sunrise(self):
        
        return self.sunrise
    
    def get_sunset(self):
        
        return self.sunset
    
    