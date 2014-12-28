#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import getpass
import subprocess
from time import sleep
from clint.textui import progress



def play_song():
	# default music
	song = "/home/{}/Music/notify.mp3".format(getpass.getuser())
	try:
		song = "{}".format(sys.argv[2])
	except IndexError:
		pass

	if not os.path.exists("/home/{}/Music/notify.mp3".format(getpass.getuser())):
		print "I am not getting the default notify.mp3 in  /home/{}/Music/notify.mp3".format(getpass.getuser())
		sys.exit()

	# mplayer
	cmd = ['mplayer','', song]
	subprocess.call('clear')
	try:
		subprocess.call(cmd)
	except OSError:
		print "Sorry to say but you need to install mplayer\n\
				sudo apt-get install mplayer"


def bar(timer):
	mock_timer = timer
	for i in progress.bar(range(timer)):
		sleep(1)



def main():
	"""
Command:
	$ timeup <sec>
	$ timeup <sec> <song>

Requirements:
	* mplayer
	* Have a \"notify.mp3\" file in your Music Folder
	"""
	try:
		timer = sys.argv[1]
		timer = int(timer)
	except:
		print "I think there might be some problem with the input...（￣へ￣）"
		print main.__doc__
		sys.exit()
	target = raw_input("What is your target? ")
	subprocess.call('clear')
	if target != "":
		print "Your target: {}\n".format(target)
	bar(timer)
	play_song()


if __name__ == "__main__":
	main()