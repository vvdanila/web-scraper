# -*- coding: utf-8 -*-

'''
##############################################################################
This script has the purpose of parsing a page from yellowpages.com and saving
the content to a JSON file.
'''
import scrapPage
import locationList
import requests
from bs4 import BeautifulSoup



# Specify the url
YP_base = "http://www.yellowpages.com"
search = "/search?search_terms=piano&geo_location_terms="
location = "New+York%2C+NY"

#locationList = locationList.locationList('wLocalities.csv')
#locationList = ["New+York%2C+NY", "Seattle%2C+WA", "Los+Angeles%2C+CA"]

# Query the website and return the html to the variable 'page'
# page = requests.get(YP_base + search + location)

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
# soup = BeautifulSoup(page.text, "lxml")

def scrapSite(location):
    scrap = []    
    loc = location
        
    #inside location
    page = requests.get(YP_base + search + loc)   
    soup = BeautifulSoup(page.text, "lxml")
    scrap += scrapPage.scrapPage(soup)
    
    #move to next page in pagination
    while True:
        try:
            tag = soup.find(class_="next ajax-page")
            nextSearch = tag['href']
        except TypeError:
            break
        
        page = requests.get(YP_base + nextSearch)
        soup = BeautifulSoup(page.text, "lxml")
        scrap += scrapPage.scrapPage(soup)
            
    return scrap

    