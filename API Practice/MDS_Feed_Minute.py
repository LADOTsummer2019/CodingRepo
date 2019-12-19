import requests
import json
import pandas as pd
import numpy as np
import csv
import time

mds_data = requests.get('https://mds.bird.co/gbfs/los-angeles/free_bikes').json()

avail_count= str(len(mds_data['data']['bikes']))
avail_time= str(mds_data['last_updated'])


# Concatenate into a row to write to the output csv file
line_something = avail_count + "," + avail_time 
# Creates new csv file
with open('outfile.csv',mode='w') as outfile: 
    outfile.write(line_something)
    outfile.write("\n")

# Timer function
def sleeper():
    # Loop
    while True:
        num = 3  # Set time here in seconds
        try:
            num = float(num)
        except ValueError:
            print('Enter in a number.\n')
            continue
            
        print('%s' % time.ctime())
        time.sleep(num)
        
        # Pull data from API
        mds_data = requests.get('https://mds.bird.co/gbfs/los-angeles/free_bikes').json()
        avail_count= str(len(mds_data['data']['bikes']))
        avail_time= str(mds_data['last_updated'])

        # Concatenate into a row to write to the output csv file
        line_something = avail_count + "," + avail_time
        
        # Append to CSV
        with open('outfile.csv',mode='a') as outfile: 
            outfile.write(line_something)
            outfile.write("\n")

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()