#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = raw_input("Enter the server: ")

def portscanner(port):
	try:
		s.connect((server,port))
		return True
	except:
		return False

for port in range(1,100):
	if portscanner(port):
		print "Port "+str(port) +" is open    ╭∩╮（︶︿︶）╭∩╮"
	else:
		print "Port "+str(port) +" is closed"
