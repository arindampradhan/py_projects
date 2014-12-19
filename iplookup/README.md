Iplookup
=============

Simple program to  look up the ip and tell about it's geolocation and all.

Install
=======

	$ python setup.py install

Usage
=====
Simply run:

	$ iplookup 208.80.152.201
	status : success
	city : San Francisco
	zip : 94105
	countryCode : US
	country : United States
	region : CA
	isp : Wikimedia Foundation
	lon : -122.3942
	timezone : America/Los_Angeles
	as : AS14907 Wikimedia Foundation Inc.
	query : 208.80.152.201
	lat : 37.7898
	org : Wikimedia Foundation
	regionName : California
	

With parameters:

	$ iplookup -json 208.80.152.201
	{
	    "status": "success", 
	    "city": "San Francisco", 
	    "zip": "94105", 
	    "countryCode": "US", 
	    "country": "United States", 
	    "region": "CA", 
	    "isp": "Wikimedia Foundation", 
	    "lon": -122.3942, 
	    "timezone": "America/Los_Angeles", 
	    "as": "AS14907 Wikimedia Foundation Inc.", 
	    "query": "208.80.152.201", 
	    "lat": 37.7898, 
	    "org": "Wikimedia Foundation", 
	    "regionName": "California"
	}

To check status:

	$ iplookup -s 208.80.152.201
	$ iplookup <parameter> <ip>
	    <parameters>
	    -status , -s
	    -city  , -c
	    -zip , -z
	    -countryCode , -cc
	    -country , -c
	    -region , -r
	    -isp , -i
	    -lon , -l
	    -timezone , -t
	    -as , -a
	    -query , -q
	    -lat , -l
	    -org ,-o
	    -regionName , -rn

