from bs4 import BeautifulSoup
import requests

url = "http://www.zillow.com/homedetails/227-Hubbell-St-Houghton-MI-49931/2131153498_zpid/"

response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.text)

# write to file
saved_soup_output = open('something2.html', 'w')
saved_soup_output.write(soup.prettify().encode('utf-8'))
saved_soup_output.close()
