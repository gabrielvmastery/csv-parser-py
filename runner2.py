from datetime import datetime
import os
import csv

HEADERS = ['Load','CompletionTime']

with open('LoadsTable.csv','r') as openFile:
    with open(str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '_mlogistics_' + '.csv','w', newline='') as csvFile:
        #writer.writerow(HEADERS)
        writer = csv.writer(csvFile, quotechar="'")#quotechar required for "" in columns (M)
        for line in openFile:
            l = line.strip('\n')
            c =  l.split(',')

            writer.writerow(c)

            print(c)

openFile.close()
csvFile.close()
