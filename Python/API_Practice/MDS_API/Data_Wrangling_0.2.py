import pandas as pd
import numpy as np
import csv
import json
import os

birdla = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/birdla.csv',sep=',',names=['count','time'])
birdla_data = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/birdla_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','time'])
birdsm = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/birdsm.csv',sep=',',names=['count','time'])
birdsm_data = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/birdsm_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','time'])
lime = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/lime.csv',sep=',',names=['count','time'])
lime_data = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/lime_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','type','time'])
spin = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/spin.csv',sep=',',names=['count','time'])
spin_data = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/spin_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','type','time'])
wheels = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/wheels.csv',sep=',',names=['count','time'])
wheels_data = pd.read_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/wheels_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','vehicleid','time'])



list0 = ['birdla.csv','birdla_data.csv','birdsm.csv','birdsm_data.csv','lime.csv','lime_data.csv','spin.csv','spin_data.csv','wheels.csv','wheels_data.csv']
list01 = ['birdla','birdsm','lime','spin','wheels']
list1 = [birdla,birdsm,lime,spin,wheels]
list2 = [birdla_data,birdsm_data,lime_data,spin_data,wheels_data]

# Save different files into one
for x in range(len(list1)):
    list1[x]['company'] = list01[x] # Create a column to store company name
    print(list1[x].head())
    list1[x].to_csv('C:/Users/LADOT-Projects/MDS/data/count_time_24hr.csv',mode='a',header=False)


''' # NEEDS TO BE FIXED
 # Saves differnet files into one
for df in range(len(list2)):
    print(list2[df].head())
    new_df = pd.DataFrame(columns=['bikeid','lat','lon','time'])
    new_df = list2[df][['bikeid','lat','lon','time',]]
    new_df['company'] = list01[df]
    new_df.append(list2[df])
    print(new_df)
    new_df.to_csv('C:/Users/LADOT/Desktop/LADOT-Projects/MDS/data/mds_data_24hrs.csv')
'''