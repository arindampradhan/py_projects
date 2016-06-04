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

from .utils import valid_city, valid_post, valid_ip
from docopt import docopt
import requests
from pprint import pprint
from utils import APP_ID
from datetime import datetime
import time

# http://openweathermap.org/current
# get the weather


def weather(city):
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast/weather?q={}&APPID={}".format(city, APP_ID))
    return r.json()


# http://stackoverflow.com/questions/2846466/how-to-convert-postal-code-to-city-name-is-there-an-api-available
# get the city from postal code using Google maps Geocoding API

def get_city_zip(zip_code):
    city_info = requests.get(
        "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false&app_id={}".format(zip_code, APP_ID))
    city_name = city_info.json()['results'][0][
        'address_components'][1]['long_name']
    return weather(city_name)


def get_city_ip(ip):
    url = 'http://ipinfo.io/' + ip + '/json'
    return requests.get(url).json()['city']


def json_parser(_json):
    # today_json = _json['list'][:5]
    # pprint(today_json)
    # print len(_json['list'])
    # print "\n\n\n\n\n\n\n"
    # print "shit"
    diffs = []
    for i in _json['list'][:5]:
        date_str = i['dt_txt']
        tym = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        now_unix = time.mktime(datetime.now().timetuple())
        time_unix = time.mktime(tym.timetuple())
        diff = abs(now_unix - time_unix)
        diffs.append(diff)

    min_index = diffs.index(min(diffs))
    lat = _json['city']['coord']['lat']
    lon = _json['city']['coord']['lon']
    country = _json['city']['country']
    description = _json['list'][min_index]['weather'][0]['description']
    speed = _json['list'][min_index]['wind']['speed']
    pressure = _json['list'][min_index]['main']['pressure']
    temp_min  =  _json['list'][min_index]['main']['temp_max'] - 273
    temp_max =  _json['list'][min_index]['main']['temp_min']  - 273
    temp = _json['list'][min_index]['main']['temp'] - 273
    humidity = _json['list'][min_index]['main']['humidity']
    print """
    Weather Updates   ☁
    description : {0}
    humidity    : {1} %
    speed       : {2}
    temperature : {3} °C
    pressure    : {4}
    latitude    : {5}
    longitude   : {6}
    country     : {7}
    max_temp    : {8} °C
    min_temp    : {9} °C
    """.format(description, humidity, speed, temp, pressure,
               lat, lon, country, temp_max, temp_min)
    print ascii_arts(description)



def parser(query, args):
    if valid_post(query):
        ans = get_city_zip(query)
        if args['--json']:
            pprint(ans)
            exit()
        else:
            print json_parser(ans)
            exit()
    if valid_ip(query):
        ans = weather(get_city_ip(query))
        if args['--json']:
            pprint(ans)
            exit()
        else:
            print json_parser(ans)
            exit()
    if valid_city(query):
        ans = weather(query)
        if args['--json']:
            pprint(ans)
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

    heavy_rain = """
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
    args = docopt(__doc__, version='weather 0.2.0')
    if args['<location>']:
        query = args['<location>']
        parser(query, args)
    else:
        print "༼ つ ◕_◕ ༽つ Not getting location dude ... "
        exit()


if __name__ == "__main__":
    main()
