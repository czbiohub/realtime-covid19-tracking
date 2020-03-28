# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executable by running 'chmod +x ./chromedriver' in directory
from selenium import webdriver
from bs4 import BeautifulSoup

sonoma = "https://socoemergency.org/"
driver = webdriver.Chrome('./chromedriver')
driver.get(sonoma)
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())

# Select Figures
activeCases = soup.findAll("p", {"class": "counterValue"})[0].contents[0]
print(activeCases)

recoveredCases = soup.findAll("p", {"class": "counterValue"})[1].contents[0]
print(recoveredCases)

num_of_tests = soup.findAll("p", {"class": "counterValue"})[3].contents[0]
print(num_of_tests)

deaths = soup.findAll("p", {"class": "counterValue"})[2].contents[0]
print(deaths)

total_pos_cases = soup.findAll("p", {"class": "counterValue"})[4].contents[0]
print(total_pos_cases)


