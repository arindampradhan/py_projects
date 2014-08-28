#mini spider web crawler

from bs4 import BeautifulSoup 
import urllib2
import requests
import urlparse

url = "http://arindam2u.com"

urls = [url]
visited = [url]

while len(urls) >0:
	try:
		page = urllib2.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(page)
	urls.pop(0)
	print len(urls)
	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])
print visited
