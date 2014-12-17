# Using http://ip-api.com/docs/api:json
# Thanks for the free Api
# USAGE
# =====
# $ python iplookup.py 
# $ python iplookup.py json

import json
import urllib2
import sys

ip = raw_input("Enter your ip address: ")

req = urllib2.urlopen("http://ip-api.com/json/"+ip).read()

json_req = json.loads(req)

try:
	if sys.argv[1] == "json":
		print json.dumps(json_req,indent=4)
except: 
	for key, value in json_req.items() :
	    print "{0} : {1}".format(key, value)

