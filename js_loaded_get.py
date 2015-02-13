# import selenium.webdriver as webdriver

# url = "http://www.youtube.com/watch?v=OuSdU8tbcHY"

# driver = webdriver.Firefox()
# driver.get(url)

# embed = driver.find_elements_by_tag_name('embed')[0]

# print embed


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
