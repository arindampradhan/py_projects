import requests
from bs4 import BeautifulSoup
# scraping http://www.littleastro.com/


def horoscope():
	soup = BeautifulSoup(requests.get("http://www.littleastro.com/").text)
	content = soup.find('ul')
	horoscopes = content.find_all('li')
	zodiacs = []
	predictions = []

	for signs in horoscopes:
		sign = signs.h3.string.split()[1]
		zodiacs.append(sign)

	for signs in horoscopes:
		prediction = signs.find('p').string
		predictions.append(prediction)

	return zip(zodiacs,predictions)


def main():
	zipup = horoscope()
	for a in zipup:
		print "# predications for",a[0]
		print "*",a[1]
		print 


if __name__ == "__main__":
	main()