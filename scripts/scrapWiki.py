# -*- coding: utf-8 -*-

'''
##############################################################################
Scrap wiki pages with localities in the US.
'''

import requests
from bs4 import BeautifulSoup
import csv

# list of all links to scrap:

linkList = [
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Alabama',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Alaska',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Arizona',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Arkansas',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Colorado',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Connecticut',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Connecticut',
    'https://en.wikipedia.org/wiki/List_of_incorporated_places_in_Delaware',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Florida',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Georgia_(U.S._state)',
    'https://en.wikipedia.org/wiki/List_of_places_in_Hawaii',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Idaho',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Illinois',
    'https://en.wikipedia.org/wiki/List_of_towns_and_villages_in_Illinois',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Indiana',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Indiana',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Iowa',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Kansas',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Kentucky',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Louisiana',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Maine',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Maryland',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Massachusetts',
    'https://en.wikipedia.org/wiki/List_of_cities,_villages,_and_townships_in_Michigan',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Minnesota',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Mississippi',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Missouri',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Montana',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Nebraska',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Nevada',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_New_Hampshire',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey',
    'https://en.wikipedia.org/wiki/List_of_populated_places_in_New_Mexico_by_population',
    'https://en.wikipedia.org/wiki/List_of_cities_in_New_York',
    'https://en.wikipedia.org/wiki/List_of_towns_in_New_York',
    'https://en.wikipedia.org/wiki/List_of_villages_in_New_York',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_North_Carolina',
    'https://en.wikipedia.org/wiki/List_of_cities_in_North_Dakota',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Ohio',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Oklahoma',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Oregon',
    'https://en.wikipedia.org/wiki/List_of_counties_in_Oregon',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Pennsylvania',
    'https://en.wikipedia.org/wiki/List_of_towns_and_boroughs_in_Pennsylvania',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Rhode_Island',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_South_Carolina',
    'https://en.wikipedia.org/wiki/List_of_towns_in_South_Dakota',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Tennessee',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Texas',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Texas',
    'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Utah',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Vermont',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Vermont',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Virginia',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Virginia',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Washington',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Washington',
    'https://en.wikipedia.org/wiki/List_of_cities_in_West_Virginia',
    'https://en.wikipedia.org/wiki/List_of_cities_in_Wisconsin',
    'https://en.wikipedia.org/wiki/List_of_towns_in_Wisconsin',
    'https://en.wikipedia.org/wiki/List_of_villages_in_Wisconsin',
    'https://en.wikipedia.org/wiki/List_of_municipalities_in_Wyoming',
]

def scrapSite(link):
    
    scrap = []    
    
        
        
    page = requests.get(link)   
    soup = BeautifulSoup(page.text, "lxml")

    
    table = soup.find_all('td')
    if table is not None:
        for el in table:
            title = el.find('a')
            try:
                loc = []
                string = title['title'].strip('"')
                loc.append(string)
                scrap.append(loc)
                continue
            except (TypeError, KeyError):
                pass

          
    return scrap






def saveFile(scrap, filename):

    with open(filename, 'a') as csvfile:
            
            writer = csv.writer(csvfile, delimiter=',',)
       
            writer.writerow(['Writer was here.'])
            for loc in scrap: 
                loc = [s.encode('utf-8') for s in loc] 
                writer.writerow(loc)


def main():
    filename = 'localities.csv'
    for link in linkList:
        scrap = scrapSite(link)
        saveFile(scrap, filename)

if __name__ == '__main__':

    main()