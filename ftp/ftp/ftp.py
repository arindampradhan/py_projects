#!/bin/python
from urlparse import urlparse
import getpass
import ftplib
import urllib
import sys

def auth():
	website  = raw_input("Website : ")
	username = raw_input("Username: ")
	passwd = getpass.getpass()
	parser = urlparse(website)
	if parser[1] == "":
		website = parser[2]
	else:
		website = parser[1]
	
	global ftp
	global user
	user = (username,passwd,website)
	ftp = ftplib.FTP(website,username,passwd)
	return user

def show():
	print "\nThe Structure of the directory:"
	print ftp.dir()

def download(filename):
	print "Retriving {0} ...".format(filename)
	urllib.urlretrieve('ftp://{0}:{1}@{2}/{3}'.format(user[0],user[1],user[2],filename),filename)

def delete(filename):
	ftp.delete(filename)
	print "Deletion complete.\n"

def upload(filename):
	print "Uploading {0} ...".format(filename)
	with open(filename,"rb") as file:
		ftp.storbinary('STOR {0}'.format(file.name), file)

def main():
	if len(sys.argv) <= 1:
		print "no parameters passed dude:\n"
		print "parameters:\n"
		print "$ pyftp show <filename> - to show the file system in server"
		print "$ pyftp del  <filename> - to delete a file"
		print "$ pyftp  -u  <filename> - to upload"
		print "$ pyftp  -d  <filename> - to download"
		print "\nThen enter the filename such as:"
		print "pyftp -u awesome.txt\n"
		exit()

	user = auth()
	if sys.argv[1] == "-d" :
		download(sys.argv[2])
	if sys.argv[1] == "-u" :
		upload(sys.argv[2])
	if sys.argv[1] == "del" :
		delete(sys.argv[2])
	if sys.argv[1] == "show" :
		show()

if __name__ == "__main__":
	main()
	ftp.close()
	exit()