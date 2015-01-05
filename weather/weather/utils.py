import socket
import re

def num_there(s):
	s = str(s)
	if any(i.isdigit() for i in s):
		return True
	else:
		return False

def valid_ip(ip):
	try:
	    socket.inet_aton(ip)
	    return True
	except (socket.error,TypeError,ValueError):
		return False

def valid_post(post_code):
	try:
		if num_there(post_code):
			return True
		else:
			return False
	except:
		return False
def valid_city(city_name):
	try:
		#using re.match() instead of re.compile()
		if num_there(city_name):
			return False
		if re.match(r'^[a-zA-Z\u0080-\u024F\s\/\-\)\(\`\.\"\']+$',city_name):
			return True
		if re.match(r'^[a-zA-Z\u0080-\u024F\s\/\-\)\(\`\.\"\']+$',city_name):
			return True
		else:
			return False
	except:
		return False