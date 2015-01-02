import urllib2
import re

name = raw_input("Enter the name of the page: ")
page = urllib2.urlopen(name).read()

titles = re.findall(r'<title>(.*?)</title>',page)
links = re.findall(r'<link.*?>(.*?)</link>',page)
descriptions =re.findall(r'<description>(.*?)</description>',page)

for title in titles:
	print title

for link in links:
	print link

for description in descriptions:
	print description