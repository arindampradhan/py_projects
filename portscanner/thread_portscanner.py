#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import threading
from Queue import Queue

print_lock = threading.Lock()

server = raw_input("Enter the server: ")
q = Queue()

def portscanner(port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		conn = s.connect((server,port))
		with print_lock:
			print "\nport "+str(port)+" is open ╭∩╮（︶︿︶）╭∩╮" 
		conn.close()
	except:
		sys.stdout.write('.')

def threader():
	while True:
		worker = q.get()
		portscanner(worker)
		q.task_done()

for x in range(50):
	t = threading.Thread(target=threader)
	t.daemon = True	
	t.start()

for worker in range(1,301):
	q.put(worker)

q.join()

