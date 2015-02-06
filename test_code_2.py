from bs4 import BeautifulSoup
import requests
import urllib2
import string
import re

url = "http://www.zillow.com/homedetails/210-Hubbell-St-Houghton-MI-49931/106383951_zpid/"
url = "http://google.com"

response = requests.get(url,s timeout=5)

soup = BeautifulSoup(response.text)

# print soup

for footer in soup.find_all("div", {'id': "footer"}):
    print footer
    print "==========================="

# print soup.prettify()

# print target[0]
# print target[1]
# result=[]
# pool=soup.find_all(id='yui_3_15_0_1_1423194225804_2307')

# print str(target[1])[:100]

# for div in soup.findAll('div', attrs={'id':'footer'}):
#     print div

# print test

# div = soup.find(attrs={'id': 'footer'})
# print type(div)
# print div
# text = " ".join(div.find_all(text=lambda t: not isinstance(t, Comment)))
# print text
# text = " ".join(text.split())
# print text
# var1, var2 = [s.strip() for s in text.split(u"\xb7")]
# print var1
# print var2
