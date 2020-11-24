from datetime import datetime
import os
import csv

HEADERS = ['Load','CompletionTime']

#outputFile = 'MasteryOutput_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.csv'

with open('LoadsTable.csv','r') as openFile:
    with open('Output2.csv','w', newline='') as csvFile:
        for line in openFile:
            l = line.strip('\n')
            c =  l.split(',')

            #for each in c:
            #    test for "" cases
            writer = csv.writer(csvFile)
#           writer.writerow(HEADERS)
            writer.writerow(c)
            print(c)

openFile.close()
csvFile.close()
