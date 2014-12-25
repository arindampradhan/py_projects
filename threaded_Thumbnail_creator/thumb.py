#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
start_time = time.time()

from PIL import Image
import os
import threading
from Queue import Queue
from glob import glob


q = Queue()


dirc  = raw_input("Enter the directory?? ")
if dirc == "" or "\n":
	dirc = "./images"


files = glob('./{}/*.gif'.format(dirc))
files.extend(glob('./{}/*.png'.format(dirc)))
files.extend(glob('./{}/*.jpg'.format(dirc)))

# thread num ratio I usually keep 5:1
lf = len(files)
thread_num = int((lf/5) + (lf/(5*5)) + (lf/(5*5*5)) )

global thumb_files
thumb_files = []

try:
	os.mkdir("thumbnail")
except:
	pass


def thumbnail_it(image_it):
	im = Image.open(image_it).resize((120,120),Image.ANTIALIAS)
	im.save("./thumbnail/{}".format(image_it.split("/")[-1]))
	thumb_files.append(image_it)
	print "image_it"


def rename():
	count = 0
	for th in os.listdir('./thumbnail'):
		os.rename("./thumbnail/"+th,"./thumbnail/{0}.{1}".format(count,th.split('.')[-1]) )
		count = count + 1	


def threader():
	while True:
		worker = q.get()
		thumbnail_it(worker)
		q.task_done()


for x in range(thread_num):
	t1 = threading.Thread(target=threader)
	t1.daemon = True
	t1.start()


for worker in files:
	q.put(worker)

q.join()
rename()

print("--- {} seconds ---".format(time.time() - start_time))