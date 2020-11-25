from datetime import datetime
import os
import csv

HEADERS = ['Load','CompletionTime']

with open('LoadsTable.csv','r') as openFile:
    with open('mastery_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.csv','w', newline='') as csvFile:
#    with open('Output2.csv','w', newline='') as csvFile:
        for line in openFile:
            l = line.strip('\n')
            c =  l.split(',')

            #for each in c:
            #    if each == ": 
            writer = csv.writer(csvFile)
            writer.writerow(c)
            print(c)

            #           writer.writerow(HEADERS)
            
openFile.close()
csvFile.close()
