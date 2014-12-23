Iplookup
=============

Simple program to  look up the ip and tell about it's geolocation and all.

Install
=======

	$ python setup.py install

Usage
=====
	iplookup -h,--help
	iplookup <ip> [ -j | -s | -z | -c | -y | -r | -i | -l | -g | -t | -q | -o | -n ]
	iplookup <repeating> ...



To check status:

	$ iplookup -s 208.80.152.201
	success

With json parameters:

	$ iplookup --json 208.80.152.201
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

