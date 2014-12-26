#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009



def broadcast(socket,sock,message):
	for socket in SOCKET_LIST:
		if socket != socket 