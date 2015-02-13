# get all listings
from bs4 import BeautifulSoup
import requests
from time import gmtime, strftime

    # Some initializations
time_string = strftime("%Y-%m-%d %H:%M:%S", gmtime())
timeout_value = 15
number_of_results = 0

# Get list of streets
url = 'http://www.zillow.com/browse/homes/mi/houghton-county/49931/'
town_page_response = requests.get(url, timeout=timeout_value)
soup = BeautifulSoup(town_page_response.text)
town = soup.find('div', attrs={'class': 'zsg-g browse-content'})
list_of_streets = town.find_all('a', href=True)

# Get list of all houses in all the streets
house_list_file = open('../secret_closet/House_list_at_' + time_string + '.txt', 'w')
for street in list_of_streets:
    number_of_results = number_of_results + 1
    street_page_response = requests.get('http://www.zillow.com' + street['href'], timeout=timeout_value)
    soup = BeautifulSoup(street_page_response.text)
    div_of_list = soup.find('main')
    list_of_houses = div_of_list.find_all('a', href=True)
    for house in list_of_houses:
        number_of_results = number_of_results + 1
        house_list_file.write("%s\n" % house['href'])
        print number_of_results, house['href']

# Finalize write
house_list_file.close()
