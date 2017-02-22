# -*- coding: utf-8 -*-

'''
##############################################################################
This script outputs the location in unicode for site scraping. 
'''

import csv

def locationList(datafile):

   
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.reader(sd)
        for line in r:
            data.append(line)
    
    newData = []

    for elem in data:
        newData.append('%2C'.join(elem).replace(' ','+'))

    return newData

   

if __name__ == '__main__':
	
	datafile = 'wLocalities.csv'

	main(datafile)