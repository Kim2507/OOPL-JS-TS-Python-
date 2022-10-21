import requests

class WeatherParser:
	"""Get weather inof"""
	#read_weather #read from jason file 
	def __init__(self,url="https://wttr.in/Boston?format=j1"):
		self.url = url
		self.r = requests.get(url)
		self.json=  r.json()

	def get_feels_like_f(self):
		read = json['current_condition'][0]['FeelsLikeF']
		return read

	#def get_cloud_cover(self):
		#read = getURL()
		#return ['current_condition'][0]['cloudcover']

	#def get_weather_description(self):
		#read = getURL()
		#return ['current_condition'][0]['weatherDesc'][0]['value']

	#def get_sunset(self):
		#read = getURL()
		#return ['weather'][0]['astronomy'][0]['sunset']

	#def get_sunrise(self):
		#read = getURL()
		#return ['weather'][0]['astronomy'][0]['sunrise']

	#def getURL():
		#r = request.get(self.url)
		#read_weather = r.json()
		#return read_weather
#print(type(get_feels_like_f))

