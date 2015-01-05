WEATHER
=======

Instant Weather updates from command line.


`Features`
============

* Takes city name ,public ip address or even the zip code.
* Returns a nice statistics for the weather.
* Even gives back the json data too.

##`Usage`
=========

### `City`

	$ weather california

		Weather Updates   ☁
		description : Sky is Clear 
		humidity    : 79
		speed       : 2.16
		temperature : 272.514  
		pressure    : 1029.61
		latitude    : 38.58
		longitude   : -121.49
		country     : United States of America
		max_temp    : 272.514
		min_temp    : 272.514


### `zip-code`

	$ weather 75121 

		Weather Updates   ☁
		description : Sky is Clear 
		humidity    : 33
		speed       : 4.51
		temperature : 307.264  
		pressure    : 1017.37
		latitude    : -34.77
		longitude   : 140.01
		country     : Australia
		max_temp    : 307.264
		min_temp    : 307.264

`More Features`
=================
### `ip` with `json`

	$ weather --json 8.8.8.8
	{u'base': u'cmc stations',
	 u'clouds': {u'all': 24},
	 u'cod': 200,
	 u'coord': {u'lat': 30.44, u'lon': -91.19},
	 u'dt': 1420438941,
	 u'id': 4337823,
	 u'main': {u'grnd_level': 1044.93,
	           u'humidity': 86,
	           u'pressure': 1044.93,
	           u'sea_level': 1047.73,
	           u'temp': 277.489,
	           u'temp_max': 277.489,
	           u'temp_min': 277.489},
	 u'name': u'',
	 u'sys': {u'country': u'United States of America',
	          u'message': 0.0034,
	          u'sunrise': 1420462942,
	          u'sunset': 1420499900},
	 u'weather': [{u'description': u'few clouds',
	               u'icon': u'02n',
	               u'id': 801,
	               u'main': u'Clouds'}],
	 u'wind': {u'deg': 2.00171, u'speed': 4.46}}
