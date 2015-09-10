import socket

def Main():
	host = '127.0.0.1'
	port = 3000
	buffer_size = 500

	server = (host,port)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(server)

	while True:
		data, addr = s.recvfrom(buffer_size)
		print "Message from " + str(addr)
		print "From connected user: " + str(data)
		data = str(data.upper())
		print "Sending: " + str(data)
		s.sendto(data,addr)
	s.close()

if __name__ == "__main__":
	Main()