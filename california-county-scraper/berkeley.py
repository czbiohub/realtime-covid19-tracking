# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executable by running 'chmod +x ./chromedriver' in directory
from selenium import webdriver
from bs4 import BeautifulSoup

berkeley = "https://www.cityofberkeley.info/coronavirus/"
driver = webdriver.Chrome('./chromedriver')
driver.get(berkeley)
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())

positiveCases = soup.find_all('strong')[0].contents[0]


