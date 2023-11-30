import glob
import pandas as pd
import os # access features of computers operating system 

# change directorty to location of files to be merged
os.chdir('data/raw_data')

# create fuction to delete leftover files after merge is complete 
def delete_file(extra_files):
    try:
        os.remove(extra_files)
    except OSError:
        pass

# identify csv files to merge by looping and express how to name new files
extension = 'csv'
csv_files = [i for i in glob.glob('*main.{}'.format(extension))]
csv_files2 = [i for i in glob.glob('*car.{}'.format(extension))]

# merge by concatenating dataframes on top of each other based on all column names matching
combined = pd.concat([pd.read_csv(f) for f in csv_files])
combined2 = pd.concat([pd.read_csv(f) for f in csv_files2])

# save new files into a new directory 
combined.to_csv('raw_merge/raw_data_main.csv', index=False)
combined2.to_csv('raw_merge/raw_data_car.csv', index=False)

# call function to delete leftover files 
for extra_files in csv_files:
    delete_file(extra_files)

for extra_files in csv_files2:
    delete_file(extra_files)