from datetime import datetime
import os
import csv

HEADERS = ['Load','CompletionTime']

with open('LoadsTable.csv','r') as openFile:
    with open('mlogic-csv-parse' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.csv','w', newline='') as csvFile:
        #writer.writerow(HEADERS)
        writer = csv.writer(csvFile)
        for line in openFile:
            l = line.strip('\n')
            c =  l.split(',')

            #for each in c:
            #    if each == ":   #test for quotes in input line and handle accordingly

            writer.writerow(c)

            print(c)

openFile.close()
csvFile.close()
