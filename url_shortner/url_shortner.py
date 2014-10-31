# requirements
# ============
# pip install beautifulsoup4
# pip install mechanize

URL = raw_input("Give me your link -> ") #url of the site
print

from bs4 import BeautifulSoup 
from mechanize import Browser

br = Browser()
br.open("http://tinyurl.com/")
br.select_form(name="f")
br['url'] = URL

response = br.submit()
soup = BeautifulSoup(response.read())
short_url = soup.find_all('blockquote')[1].find('a')['href'] #scraped the page to get the url
print short_url