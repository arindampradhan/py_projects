import socket

def Main():
	host = '127.0.0.1'
	port = 3001
	buffer_size = 500

	server = (host,3000)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	
	s.bind((host,port))
	message = raw_input("Enter message: ")
	while message != "q":
		s.sendto(message,server)
		data,addr = s.recvfrom(buffer_size)
		print "Receive from server " + str(data)
		message = raw_input("Enter message: ")
	s.close()

if __name__ == "__main__":
	Main()