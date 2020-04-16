import webdriver from selenium 
import time
import urllib
import urllib2

x=raw_input("https://www.coingecko.com/en")
refreshrate=raw_input("5")
refreshrate=int(refreshrate)
driver = webdriver.Firefox()
driver.get("http://"+x)
while True:
    time.sleep(refreshrate)
    driver.refresh()