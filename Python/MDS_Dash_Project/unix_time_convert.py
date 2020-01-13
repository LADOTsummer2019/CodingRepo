import os
import pandas as pd
import csv

desiredpath = 'C:/Users/406822/Desktop/MDS_data/'
os.chdir(desiredpath)
print(desiredpath)


data = 'count_15min.csv'
df = pd.read_csv(data)
# print(df.head())
df['new_date'] = pd.to_datetime(df['unixtime'],unit='s') # Check time/date
print(df.head())
df.to_csv('new_date.csv')

