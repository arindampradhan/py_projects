import socket

def Main():
	host = '127.0.0.1'
	port = 5000
	buffer_size = 50

	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c,addr = s.accept()

	print "Connection located at", str(addr)
	while True:
		data = c.recv(buffer_size)
		if not data:break
		print "from the user" + str(data)
		data = str(data).upper()
		print data
		c.send(data)
	c.close()

if __name__ == "__main__":
	Main()