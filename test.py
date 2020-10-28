from datetime import datetime
import os
file_path = <PASS YOUR FILE HERE>
outputFile = 'ML_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.csv'

with open('H:\Results.csv','r') as openFile:
    with open('H:\Output.csv','w') as writeFile:
        for line in openFile:
            #split line by comma and compare first column, can be modified depending on given file            
            cleanline = line.strip('\n')
            column =  cleanline.split(',')



