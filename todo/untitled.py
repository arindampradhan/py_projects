import requests

# get the weather

def weather(place): 
	r = requests.get()
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}'.format(place))



# 