# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://coronavirus.marinhhs.org/" 
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

positiveCases = soup.body.find("table").find_all('td')[5].contents[0]
updatedAt = deathsRaw = soup.find("div", {"class": "view-footer"}).contents[0]
