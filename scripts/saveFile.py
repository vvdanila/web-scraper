# -*- coding: utf-8 -*-

'''
##############################################################################
Print to CSV file

To add Washington D.C. manually as a location
'''
import locationList
import csv
import scrapSite





def saveFile(scrap, filename):

    with open(filename, 'a') as csvfile:
            
            writer = csv.writer(csvfile, delimiter=',',)
        
            # writer.writerow(['Name', 'Address', 'Locality',
            #                  'Region', 'Postal Code', 'Telephone',
            #                  'Website', 'Category'
            # ])
            for list in scrap:
                list = [s.encode('utf-8') for s in list]
                writer.writerow(list)


if __name__ == '__main__':

    filename = 'secondTest.csv'
    locationList = locationList.locationList('wLocalities.csv')
    
    for loc in locationList:
        scrap = scrapSite.scrapSite(loc)
        saveFile(scrap, filename)