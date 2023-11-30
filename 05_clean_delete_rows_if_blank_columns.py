import pandas as pd
import numpy as np


df1 = pd.read_csv('data/raw_data/raw_merge/raw_data_car.csv')


# add NaN if blank column 
df1['ModelDescription'].replace('', np.nan, inplace=True)
df1['MakeDescription'].replace('', np.nan, inplace=True)

# drop rows if NaN 
df1 = df1.dropna(subset=['ModelDescription', 'MakeDescription']) 

# drop any rows that are identical 
df1 = df1.drop_duplicates(keep='first') # first indicates to keep first duplicate and remove the rest
# reset index
df1 = df1.reset_index(drop=True)
# name index
df1.index.name = 'Index'

df1.to_csv('data/clean_data/clean_data_car.csv') # allow index