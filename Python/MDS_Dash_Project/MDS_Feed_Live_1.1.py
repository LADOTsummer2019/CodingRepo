import os
import requests
import pandas as pd
import json
import time
import numpy as np

# change directory
desiredpath = 'C:/Users/406822/Desktop/tim_black_mds/'
os.chdir(desiredpath)
print(desiredpath)


def sleeper():
    while True:
        num = (300-8)    # Sleep for 15 minutes
        try:
            num = float(num)
        except ValueError:
            print('Enter in a number.\n')
            continue
        
        # Pulls from api
        print('%s' % time.ctime())
        _wheels = requests.get('https://la-gbfs.getwheelsapp.com/free_bike_status.json').json()
        _lime = requests.get('https://lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status.json').json()
        _birdla = requests.get('https://mds.bird.co/gbfs/los-angeles/free_bikes').json()
        _birdsm = requests.get('https://mds.bird.co/gbfs/santamonica/free_bikes').json()
        _spin = requests.get('https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json').json()

        # Store all data to df
        wheels_df = pd.DataFrame(_wheels['data']['bikes'])
        lime_df = pd.DataFrame(_lime['data']['bikes'])
        birdla_df = pd.DataFrame(_birdla['data']['bikes'])
        birdsm_df = pd.DataFrame(_birdsm['data']['bikes'])
        spin_df = pd.DataFrame(_spin['data']['bikes'])

        # Create new column
        wheels_df['time'] = _wheels['last_updated']
        lime_df['time'] = _lime['last_updated']
        birdla_df['time'] = _birdla['last_updated']
        birdsm_df['time'] = _birdsm['last_updated']
        spin_df['time'] = _spin['last_updated']

        # Save to csv
        wheels_df.to_csv('wheels_data.csv',mode='a',header=False)
        lime_df.to_csv('lime_data.csv',mode='a',header=False)
        birdla_df.to_csv('birdla_data.csv',mode='a',header=False)
        birdsm_df.to_csv('birdsm_data.csv',mode='a',header=False)
        spin_df.to_csv('spin_data.csv',mode='a',header=False)

        # Pull count
        wheels_count= str(len(_wheels['data']['bikes']))
        lime_count= str(len(_lime['data']['bikes']))
        birdla_count= str(len(_birdla['data']['bikes']))
        birdsm_count= str(len(_birdsm['data']['bikes']))
        spin_count= str(len(_spin['data']['bikes']))

        # Pull time
        wheels_time= str(_wheels['last_updated'])
        lime_time= str(_lime['last_updated'])
        birdla_time= str(_birdla['last_updated'])
        birdsm_time= str(_birdsm['last_updated'])
        spin_time= str(_spin['last_updated'])

        # Concatenate into a row to write to the output csv file
        wheels = wheels_count + "," + wheels_time
        lime = lime_count + "," + lime_time
        birdla = birdla_count + "," + birdla_time
        birdsm = birdsm_count + "," + birdsm_time
        spin = spin_count + "," + spin_time

        # Append to time_count.csv
        with open('wheels.csv',mode='a') as outfile: 
            outfile.write(wheels)
            outfile.write("\n")
        with open('lime.csv',mode='a') as outfile: 
            outfile.write(lime)
            outfile.write("\n")
        with open('birdla.csv',mode='a') as outfile: 
            outfile.write(birdla)
            outfile.write("\n")
        with open('birdsm.csv',mode='a') as outfile: 
            outfile.write(birdsm)
            outfile.write("\n")    
        with open('spin.csv',mode='a') as outfile: 
            outfile.write(spin)
            outfile.write("\n")

        print('%s' % time.ctime())

        time.sleep(num)

try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
