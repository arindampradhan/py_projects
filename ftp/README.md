ftp program
=============

A Simple command line tool for basic ftp operation. 


Usage:
=====
* **show:** shows the server directory.
* **del:** deletes a file in the directory.
* **-d:** downloads the file from the server.
* **-u:** uploads the file to the server.


Command:
=======

	$ pyftp show
	Website : yourdomain.com
	Username: <username>
	Password: 

	the structure of the directory:
	drwxr-x---    3 username      12               	  4096 Nov 23 12:28 etc
	drwx------    2 username      username            4096 Dec 15 05:09 logs
	drwxr-x---    8 username      username            4096 Nov 23 12:08 mail
	drwxr-x---    3 username      username            4096 Dec 14 18:32 ftp
	drwxr-x---   12 username      99               	  4096 Nov 23 12:36 html
	-rw-r--r--    1 username      username             952 Dec 15 07:05 www
	-rw-r--r--    1 username      username               0 Dec 15 05:51 file.txt
	drwxr-xr-x    8 username      username            4096 Nov 23 12:25 tmp


	$ pyftp del file.txt
	Website : yourdomain.com
	Username: <username>
	Password: 
	Deletion complete.

	$ pyftp -u file.txt
	Website : yourdomain.com
	Username: <username>
	Password: 
	Uploading file.txt ...
	Uploade complete.

	$ pyftp -d file.txt 
	Website : yourdomain.com
	Username: <username>
	Password: 
	Retriving file.txt ...
