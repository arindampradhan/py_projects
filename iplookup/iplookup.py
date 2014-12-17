# using http://ip-api.com/docs/api:json
# thanks for the api
# http://ip-api.com/json/208.80.152.201?callback=yourfunction

import json
import urllib2

ip = raw_input("Enter your ip address: ")

req = urllib2.urlopen("http://ip-api.com/json/"+str(ip)).read()

json_req = json.loads(req)

for key, value in json_req.items() :
    print "{0} : {1}".format(key, value)
