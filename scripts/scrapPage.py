# -*- coding: utf-8 -*-

'''
##############################################################################
This is a script to scrape an individual page.
'''



def scrapPage(soup):
    
    infoTag = soup.find_all('div')
    returnList = []
    
    for el in infoTag: 
        
        tempList = []
        
        try:
            if el['class'] == ['info']:
                
                try:
                    name = el.find(itemprop="name")
                    tempList.append(name.text)
                except AttributeError:
                    tempList.append(name.text)

                try:
                    address = el.find(itemprop="streetAddress")
                    tempList.append(address.text)
                except AttributeError:
                    tempList.append('NA')

                try:
                    locality = el.find(itemprop="addressLocality")
                    tempList.append(locality.text)
                except AttributeError:
                    tempList.append('NA')

                try:
                    region = el.find(itemprop="addressRegion")
                    tempList.append(region.text)
                except AttributeError:
                    tempList.append('NA')

                try:
                    postalCode = el.find(itemprop="postalCode")
                    tempList.append(postalCode.text)
                except AttributeError:
                    tempList.append('NA')

                try:
                    telephone = el.find(itemprop="telephone")
                    tempList.append(telephone.text)
                except AttributeError:
                    tempList.append('NA')

                url = el.find(class_="track-visit-website")
                try:
                    tempList.append(url['href'])
                except TypeError:
                    tempList.append('NA')

                try:
                    categories = el.find(class_="categories")
                    tempList.append(categories.text)
                except:
                    tempList.append('NA')
            
            if tempList:
                returnList.append(tempList)

        except KeyError:
            pass
    
    return returnList
   

