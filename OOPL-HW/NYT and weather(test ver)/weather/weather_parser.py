
class WeatherParser:
	"""Get weather info"""
	"""pass in url and get info from that url """
	def __init__(self,url=''):
		self.url = url

	def get_json_object(self,puller):
		r = puller.get(self.url)
		json = r.json()
		return json

	"""get info about the temperature feel liks"""
	def get_feels_like_f(self,json_reader=''):
		json_reader = json_reader['current_condition'][0]['FeelsLikeF']
		return json_reader

	"""Get cloud cover condition"""
	def get_cloud_cover(self,json_reader):
		json_reader = json_reader['current_condition'][0]['cloudcover']
		return json_reader

	"""Get weather description"""
	def get_weather_description(self,json_reader):
		json_reader = json_reader['current_condition'][0]['weatherDesc'][0]['value']
		return json_reader

	"""get sunset time"""
	def get_sunset(self,json_reader):
		json_reader = json_reader['weather'][0]['astronomy'][0]['sunset']
		return json_reader

	"""Get sunrise time"""
	def get_sunrise(self,json_reader):
		json_reader = json_reader['weather'][0]['astronomy'][0]['sunrise']
		return json_reader




