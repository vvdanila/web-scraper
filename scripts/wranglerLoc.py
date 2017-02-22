# -*- coding: utf-8 -*-

'''
##############################################################################
Wrangle localities from localities.csv
'''
import csv

def main(datafile, filename):

   
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.reader(sd)
        for line in r:
            data.append(line)
    
    newData = []

    for elem in data:
        if elem not in newData:
            newData.append(elem)

    data = newData
    

    with open(filename, 'a') as csvfile:
            
        writer = csv.writer(csvfile, delimiter=',',)
   
        #writer.writerow(['Writer was here.'])
        for elem in data: 
            #elem = [s.encode('utf-8') for s in elem] 
            writer.writerow(elem)

if __name__ == '__main__':

    datafile = 'localities.csv'
    filename = 'wLocalities.csv'

    main(datafile, filename)