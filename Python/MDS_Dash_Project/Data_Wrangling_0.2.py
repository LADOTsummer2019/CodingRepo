import os
import pandas as pd
import numpy as np
import csv
import json

# change directory
desiredpath = 'C:/Users/406822/Desktop/tim_black_mds/'
os.chdir(desiredpath)
print(desiredpath)


birdla = pd.read_csv('birdla.csv',sep=',',names=['count','time'])
birdla_data = pd.read_csv('birdla_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','time'])
birdsm = pd.read_csv('birdsm.csv',sep=',',names=['count','time'])
birdsm_data = pd.read_csv('birdsm_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','time'])
lime = pd.read_csv('lime.csv',sep=',',names=['count','time'])
lime_data = pd.read_csv('lime_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','type','time'])
spin = pd.read_csv('spin.csv',sep=',',names=['count','time'])
spin_data = pd.read_csv('spin_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','type','time'])
wheels = pd.read_csv('wheels.csv',sep=',',names=['count','time'])
wheels_data = pd.read_csv('wheels_data.csv',sep=',',names=['bikeid','is_reserved','is_disabled','lat','lon','vehicleid','time'])


list0 = ['birdla.csv','birdla_data.csv','birdsm.csv','birdsm_data.csv','lime.csv','lime_data.csv','spin.csv','spin_data.csv','wheels.csv','wheels_data.csv']
list01 = ['birdla','birdsm','lime','spin','wheels']
list02 = ['birdla_data','birdsm_data','lime_data','spin_data','wheels_data']
list1 = [birdla,birdsm,lime,spin,wheels]
list2 = [birdla_data,birdsm_data,lime_data,spin_data,wheels_data]


# Create new files with header
col_head0 = ['count','unixtime','company'] # How to create headers ?????????
col_head1 = ['bikeid','lat','lon','unixtime','company']
df = pd.DataFrame(columns=col_head0)
df2 = pd.DataFrame(columns=col_head1)
df.to_csv('count_time_1min.csv')
df2.to_csv('test.csv')


# Saves counts and time into one file
for x in range(len(list1)):
    list1[x]['company'] = list01[x] # Create a column to store company name
    list1[x].to_csv('count_time_1min.csv',mode='a',header=False)
df = pd.read_csv('count_time_1min.csv')


'''
# Saves mds data into one file
# FIXED CODE BELOW
for df in range(len(list2)):
    print(list2[df].head())
    new_df = pd.DataFrame(columns=['bikeid','lat','lon','time'])
    new_df = list2[df][['bikeid','lat','lon','time',]]
    new_df['company'] = list01[df]
    new_df.append(list2[df])
    print(new_df)
    new_df.to_csv('mds_data_24hrs.csv')
'''

for y in range(len(list2)):
    list2[y]['company'] = list01[y]
    new_df = pd.DataFrame(columns=['bikeid','lat','lon','time','company'])
    new_df = list2[y][['bikeid','lat','lon','time','company']]
    new_df.to_csv('test.csv',mode='a',header=False)
