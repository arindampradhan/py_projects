import requests
from pprint import pprint

postal_address = raw_input("Enter the city name: ")
APPID = raw_input("Enter APP_ID/api-key from the website: ")


# http://openweathermap.org/current
# get the weather
def weather(city):
	r = requests.get("http://api.openweathermap.org/data/2.5/forecast/weather?q={}&APPID={}".format(city,APPID))
	return r


pprint(weather(postal_address).json())
