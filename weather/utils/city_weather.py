import requests
from pprint import pprint

postal_address = raw_input("Enter the city name: ")


# http://openweathermap.org/current
# get the weather
def weather(city): 
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}'.format(city))
	return r


pprint(weather(postal_address).json())