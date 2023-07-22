import pandas as pd
import csv
# with open('google_play_store_data.csv','r') as f:
#      result=csv.reader(f,delimiter=',')
data=pd.read_csv('google_play_store_data.csv')
print(data.isnull().sum())
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')
data['Rating'].fillna(data['Rating'].mean(),inplace=True)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

print(data['Rating'])
