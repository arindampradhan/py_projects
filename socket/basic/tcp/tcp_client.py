import socket

def Main():
	host = '127.0.0.1'
	port = 5000
	buffer_size = 50

	s = socket.socket()
	s.connect((host,port))

	message = raw_input('type your message: ')
	while message != "q":
		s.send(message)
		data = s.recv(buffer_size)
		print "Received from server: " + str(data)
		message = raw_input("type your message: ")
	s.close()

if __name__ == "__main__":
	Main()