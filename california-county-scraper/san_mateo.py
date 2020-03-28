# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executable by running 'chmod +x ./chromedriver' in directory
from selenium import webdriver
from bs4 import BeautifulSoup

san_mateo = "https://www.smchealth.org/coronavirus"
driver = webdriver.Chrome('./chromedriver')
driver.get(san_mateo)
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())

# Select Figures

positiveCases_table  = soup.find_all("table")[0] #{"clas: "contacts_table"}).div.select('em')[0].contents[0] #alameda

#positiveCases = positiveCases_table.find('td').find_next_sibling('td').text this is one way of doing it
positiveCases = soup.find_all("table")[0].find_all('td')[1].text
print(positiveCases)

deaths = soup.find_all("table")[0].find_all('td')[3].text
print(deaths)



