#!/usr/bin/env python
# -*- coding: utf-8 *-

# Using http://ip-api.com/docs/api:json
# Thanks for the free Api
# USAGE
# =====
# $ iplookup <ip>

import json
import urllib2
import sys

def parser(json_req,mode):
	"""
	$ iplookup <parameter> | <ip>

	Not getting any ip dude ¯\_(ツ)_/¯

	eg. google ip: 64.233.160.0
	$ iplookup 64.233.160.0

	Optional arguments: <parameter>
	-k, -json 			show the json file of the lookup
	-s, -status			show the status,if available or not
	-c, -city			show the location where the ip is located
	-z, -zip			show the zip code the the ip
	-c, -countryCode		show the countrycode of the ip
	-c, -country 			show the country where the ip is located
	-r, -region 			show the region of the ip
	-i, -isp			show the organization or the foundation
	-l, -lon 			show the longitude
	-t, -timezone			show the timezone
	-a, -as 			show the Incorporation
	-q, -query			show the query you made
	-l, -lat 			show the latitude of the location
	-o, -org 			show the organization
	-r, -regionName 		show the regionName
	"""
	# really not pythonic :( I know, but argparse sucks!!

	if mode[0] == "-":
		mode = mode[1:]
		if mode.lower() == "j":
			return json.dumps(json_req)
		if mode.lower() == "json":
			return json.dumps(json_req,indent=4)
		if mode in ("status","s"):
			return json_req["status"]
    	if mode in ("city","c"):
			return json_req["city"]
    	if mode in ("zip","z"):
			return json_req["zip"]
    	if mode in ("countryCode","cc"):
			return json_req["countryCode"]
    	if mode in ("country","c"):
			return json_req["country"]
    	if mode in ("region","r"):
			return json_req["region"]
    	if mode in ("isp","i"):
			return json_req["isp"]
    	if mode in ("lon","l"):
			return json_req["lon"]
    	if mode in ("timezone","t"):
			return json_req["timezone"]
    	if mode in ("as","a"):
			return json_req["as"]
    	if mode in ("query","q"):
			return json_req["query"]
    	if mode in ("lat","l"):
			return json_req["lat"]
    	if mode in ("org","o"):
			return json_req["org"]
    	if mode in ("regionName","rn","rN"):
    		return json_req["regionName"]
	else:
		print "No such parameter available dude ｍ（．＿．）ｍ"
		sys.exit()

def _build_json(ip):
	req = urllib2.urlopen("http://ip-api.com/json/{}".format(ip)).read()
	json_req = json.loads(req)
	return json_req

def main():
	if len(sys.argv) < 2:
		print parser.__doc__
		sys.exit()
	if len(sys.argv) == 2:
		json_req = _build_json(sys.argv[1])
		for key, value in json_req.items() :
		    print "{0} : {1}".format(key, value)
	if len(sys.argv) == 3:
		json_req = _build_json(sys.argv[2])
		print parser(json_req,sys.argv[1])

if __name__ == "__main__":
	main()
