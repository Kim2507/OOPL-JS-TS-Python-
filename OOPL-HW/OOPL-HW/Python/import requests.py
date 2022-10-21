import requests

"""url ='https://wttr.in/HoChiMinh?format=j1'

print(f"Getting live data from {url}")

r = requests.get(url)
weather_report=  r.json()

print(f"Sunset: {weather_report['weather'][0]['astronomy'][0]['sunset']}")"""


#Function to take url and return sunset time 
def sunset(url):
	try:
		r= requests.get(url)
		#weather = r.json()
		#sunset = weather['weather'][0]['astronomy'][0]['sunset']
		#return sunset
	except NameError:
		result ="The director does not exist..."
		return result
	weather = r.json()
	sunset = weather['weather'][0]['astronomy'][0]['sunset']
	return sunset



url ='https://wttr.in/HoChiMinh?format=j1'
invalid_url = '7237192.com'
print(sunset(url))
print(sunset(invalid_url))