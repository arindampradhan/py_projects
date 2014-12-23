#!/usr/bin/env python
# -*- coding: utf-8 *-

# Using http://ip-api.com/docs/api:json
# Thanks for the free Api
# Whois API charge a lot   t ( - _ - t )
# USAGE
# =====
# $ iplookup <ip>

""" iplookup
    
    Usage:
        iplookup -h,--help
        iplookup <ip> [ -j | -s | -z | -c | -y | -r | -i | -l | -g | -t | -q | -o | -n ]
        iplookup <repeating> ...

    Options:
        -h,--help       : show this help message
        ip        : example of a ip argument
        repeating       : example of repeating arguments
        -j,--json       : show the json file of the lookup
        -s,--status     : show the status,if available or not
        -z,--zip        : show the zip code the the ip
        -c,--country    : show the country where the ip is located
        -y,--city       : show the location where the ip is located
        -r,--region     : show the region of the ip
        -i,--isp        : show the organization or the foundation
        -l,--lat        : show the latitude of the location
        -t,--timezone   : show the timezone 
        -q,--query      : show the query you made
        -o,--org        : show the organization
        -n,--lon        : show the longitude
        -g,--regionName   : show the timezone 
"""
from docopt import docopt
from docopt import sys
import urllib2
import json

def parser(json_req,args):
	if args['--json']:
		print json.dumps(json_req,indent=4)
	if args['--status']:
		print json_req['status']
	if args['--zip']:
		print json_req['zip']
	if args['--country']:
		print json_req['country']
	if args['--region']:
		print json_req['region']
	if args['--isp']:
		print json_req['isp']
	if args['--lon']:
		print "lon: ",json_req['lon']
	if args['--lat']:
		print json_req['lat']
	if args['--timezone']:
		print json_req['timezone']
	if args['--query']:
		print json_req['query']
	if args['--org']:
		print json_req['org']
	if args['--lon']:
		print json_req['lon']
	if args['--regionName']:
		print json_req['regionName']
	if args['<ip>'] and (len(sys.argv) == 2):
		for key, value in json_req.items() :
		    print "{0} : {1}".format(key, value)

def _build_json(ip):
	req = urllib2.urlopen("http://ip-api.com/json/{}".format(ip)).read()
	json_req = json.loads(req)
	return json_req

def main():
	args = docopt(__doc__,version='iplookup 0.2.0')
	if args['<ip>']:
		json_req = _build_json(args['<ip>'])
		parser(json_req,args)
	else:
		print "Not getting any ip dude ¯\_(ツ)_/¯"
		exit

if __name__ == "__main__":
	main()