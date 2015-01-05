#!/usr/bin/env python
# -*- coding: utf-8 *-

""" weather Updates
    
    Usage:
        weather -h,--help
       	weather <location> [ -j ]
        weather <repeating> ...

    Options:
        -h,--help       : show this help message
        location        : location can be an ip address ,zip-code or city name
        repeating       : example of repeating arguments
        -j,--json       : show the json file of the lookup
"""

from .utils import valid_city,valid_post,valid_ip
from docopt import docopt
import requests
from pprint import pprint

# http://openweathermap.org/current
# get the weather
def weather(city): 
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}'.format(city))
	return r.json()


# http://stackoverflow.com/questions/2846466/how-to-convert-postal-code-to-city-name-is-there-an-api-available
# get the city from postal code using Google maps Geocoding API
def get_city_zip(zip_code):
	city_info = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(zip_code))
	city_name = city_info.json()['results'][0]['address_components'][1]['long_name']
	return weather(city_name)


def get_city_ip(ip):
	url = 'http://ipinfo.io/' + ip + '/json'
	return requests.get(url).json()['city']


def json_parser(_json):
	lat = _json['coord']['lat']
	lon = _json['coord']['lon']
	description = _json['weather'][0]['description']
	speed = _json['wind']['speed']
	country = _json['sys']['country']
	pressure = _json['main']['pressure']
	temp_min = _json['main']['temp_max']
	temp_max = _json['main']['temp_min']
	temp = _json['main']['temp']
	humidity = _json['main']['humidity']
	print """
	Weather Updates   ☁
	description : {0} 
	humidity    : {1}
	speed       : {2}
	temperature : {3}  
	pressure    : {4}
	latitude    : {5}
	longitude   : {6}
	country     : {7}
	max_temp    : {8}
	min_temp    : {9}
	""".format(description,humidity,speed,temp,pressure,\
		lat,lon,country,temp_max,temp_min)
	print "shit"

def parser(query,args):
	if valid_post(query):
		ans = get_city_zip(query)
		if args['--json']:
			pprint (ans)
			exit()
		else:
			print json_parser(ans)
			exit()
	if valid_ip(query):
		ans = weather(get_city_ip(query))
		if args['--json']:
			pprint (ans)
			exit()
		else:
			print json_parser(ans)
			exit()
	if valid_city(query):
		ans = weather(query)
		if args['--json']:
			pprint (ans)
			exit()
		else:
			print json_parser(ans)
			exit()


def ascii_arts(weath_type):
	rain = """
	   _( )_          _     
   _(     )_      _( )_
  (_________)   _(     )_
    \  \  \    (_________)
      \  \       \  \  \
                   \  \

	"""

	heavy_rain="""
	, // ,,/ ,.// ,/ ,// / /, // ,/, /, // ,/,
	/, // ,/,_|_// ,/ ,, ,/, // ,/ /, //, /,/
	 /, /,.-'   '-. ,// ////, // ,/,/, // ///
	, ,/,/         \ // ,,///, // ,/,/, // ,
	,/ , ^^^^^|^^^^^ ,// ///  /,,/,/, ///, //
	 / //     |  O    , // ,/, //, ///, // ,/
	,/ ,,     J\/|\_ |+'(` , |) ^ ||\|||\|/` |
	 /,/         |   || ,)// |\/-\|| ||| |\] .
	/ /,,       /|    . ,  ///, . /, // ,//, /
	, /         \ \    ). //, ,( ,/,/, // ,/,	
	"""

	cloudy = """
	              (`  ).                   _
             (     ).              .:(`  )`.
)           _(       '`.          :(   .    )
        .=(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .+(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.-(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.
	"""

	sunny = """
,--.::::::::::::::::::::::::::::::::::::....:::::::
    )::::::::::::::::::::::::::::::::..      ..::::
  _'-. _:::::::::::::::::::::::::::..   ,--.   ..::
 (    ) ),--.::::::::::::::::::::::.   (    )   .::
             )-._::::::::::::::::::..   `--'   ..::
_________________):::::::::::::::::::..      ..::::
::::::::::::::::::::::::::::::::::::::::....:::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::	
	"""

def main():
	args = docopt(__doc__,version='weather 0.2.0')
	if args['<location>']:
		query = args['<location>']
		parser(query,args)
	else:
		print "༼ つ ◕_◕ ༽つ Not getting location dude ... "
		exit()


if __name__ == "__main__":
	main()
