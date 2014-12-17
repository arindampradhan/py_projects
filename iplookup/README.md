Lines Of Code
=============

Simple program to  look up the ip and tell about it's geolocation and all.


Usage
=====
Simply run:
	$ python iplookup.py
	Enter your ip address: 208.80.152.201
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
	
	$ python iplookup.py json
	Enter your ip address: 208.80.152.201
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
