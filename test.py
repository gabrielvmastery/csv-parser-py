from datetime import datetime
import os
import csv
#file_path = <PASS YOUR FILE HERE>
HEADERS = ['Load','CompletionTime']

outputFile = 'MasteryOutput_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.csv'

with open('LoadsTable.csv','r') as openFile:
    with open('Output2.csv','w', newline='') as csvFile:
        for line in openFile:
            l = line.strip('\n')
            c =  l.split(',')

            #for each in c:
            #    print(each)
            writer = csv.writer(csvFile)
#           writer.writerow(HEADERS)
            writer.writerow(c)

openFile.close()
csvFile.close()
