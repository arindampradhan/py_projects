from threading import Thread
import urllib2

def th(ur):
	htmltext = urllib2.urlopen(ur).read()
	print htmltext[0:100]


urls = "http://google.com http://cnn.com http://yahoo.com http://wikipedia.com".split()

threadlist = []

for u in urls:
	t = Thread(target=th,args=(u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()
