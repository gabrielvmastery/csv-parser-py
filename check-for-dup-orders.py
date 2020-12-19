from datetime import datetime
import os
import csv

with open('all-mm-orders.csv','r') as openFile:
    with open(str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '_mlogistics_' + '.csv','w', newline='') as csvFile:
        #writer.writerow(HEADERS)
        writer = csv.writer(csvFile, quotechar="'")#quotechar required for "" in columns (M)
        seen = set()
        for line in openFile:
        #    l = line.strip('\n')
        #    c =  l.split(',')

            if line in seen:
                csvFile.write(line)
                #writer.writerow(line)
                print(line)
            seen.add(line)
        #print(seen)
openFile.close()
csvFile.close()
