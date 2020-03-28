# -*- coding: utf-8 -*-

# Imports. Make sure webdriver is executableby running 'chmod +x ./chromedriver' in directory
 
from selenium import webdriver
from bs4 import BeautifulSoup
alameda = "http://www.acphd.org/2019-ncov.aspx" 
driver = webdriver.Chrome('./chromedriver')
driver.get(alameda)
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())
# Select Figures
positiveCasesRaw = soup.find("table", {"class": "contacts_table"}).div.select('em')[0].contents[0]
deathsRaw = soup.find("table", {"class": "contacts_table"}).div.select('em')[1].contents[0]

# Remove *
positiveCasesClean = positiveCasesRaw.replace("*", "")
deathsClean = positiveCasesRaw.replace("*", "")
print("Num of positive cases in Alameda County" + positiveCasesClean)
print(deathsClean)

