import pandas as pd
from datetime import datetime # module that specializes handeling date/time specific data

# read in files 
df1 = pd.read_csv('data/raw_data/raw_merge/raw_data_main.csv')
df2 = pd.read_csv('data/raw_data/raw_merge/raw_data_car.csv')

#  add date and time to car data 
df2 = df2.merge(df1[['IncidentID', 'CollisionTime', 'CollisionDate']], on='IncidentID', how='left')

# change date format for both data sets
df1['CollisionDate'] = pd.TimedeltaIndex(df1['CollisionDate'], unit='d') + datetime(1899, 12, 30)
df2['CollisionDate'] = pd.TimedeltaIndex(df2['CollisionDate'], unit='d') + datetime(1899, 12, 30)

# change time to represent only the hour that collision took place
df1['CollisionTime'] = pd.to_datetime(df1['CollisionTime'], errors='coerce', format='%H%M').dt.hour
df2['CollisionTime'] = pd.to_datetime(df2['CollisionTime'], errors='coerce', format='%H%M').dt.hour

# add an hour column to pin point hour of a collision
#df1['Hour'] = df1['CollisionTime'] + pd.Timedelta(hours=1)
#df1['Hour'] = df1['CollisionTime'].dt.hour


# add day of week to main data
df1['CollisionDate'] = pd.to_datetime(df1['CollisionDate']) 
df1['DayofWeek'] = df1['CollisionDate'].dt.day_name()


# sort both data frames by date
df1 = df1.sort_values('CollisionDate')
df2 = df2.sort_values('CollisionDate')

# save files 
df1.to_csv('data/raw_data/raw_merge/raw_data_main.csv', index=False)
df2.to_csv('data/raw_data/raw_merge/raw_data_car.csv', index=False)

