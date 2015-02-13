# parser

from bs4 import BeautifulSoup
import re

url = open('something.html', 'r').read()
soup = BeautifulSoup(url)

info = soup.find('section', attrs={'class': 'zsg-content-section '})
print info.prettify()
print '------------------------------'

lists = info.find_all('li')
for li in lists:
    print li.get_text()
    if li.find(text=re.compile('Lot')) is not None:
        lot = li.find(text=re.compile('Lot')).lstrip()
    if li.find(text=re.compile('days on Zillow')) is not None:
        days_on_zillow = li.find(text=re.compile('days on Zillow')).lstrip()
    if li.find(text=re.compile('Price/sqft')) is not None:
        price_per_sqft = li.find(text=re.compile('Price/sqft')).lstrip()
    if li.find(text=re.compile('Room count')) is not None:
        rooms = li.find(text=re.compile('Room count')).lstrip()
    if li.find(text=re.compile('Floor size')) is not None:
        area = li.find(text=re.compile('Floor size')).lstrip()
    if li.find(text=re.compile('Zillow Home ID')) is not None:
        zillow_id = li.find(text=re.compile('Zillow Home ID')).lstrip()

print '--------------------------------'
print int(re.findall('\d+', lot.replace(",", ""))[0])
print lot, days_on_zillow, price_per_sqft, rooms, area, zillow_id
