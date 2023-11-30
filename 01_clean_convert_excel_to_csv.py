import pandas as pd # used to handle data 
import glob # used to search for specifc files that match a pattern or name

# convert individual excel files into individual csv files
excel_files = glob.glob('data/raw_data/*.xlsx') # grab all excel files and assume the path
for excel in excel_files: # loop through all excel files
    csv_out = excel.split('.')[0]+'_main.csv' # keep names same as orginal files
    csv_out2 = excel.split('.')[0]+'_car.csv' # keep names same as orginal files
    df = pd.read_excel(excel) # if only the first csv sheet is needed
    df2 = pd.read_excel(excel, sheet_name='Vehicle')
    df.to_csv(csv_out, index=False) # make conversion one file at a time
    df2.to_csv(csv_out2, index=False)
# csv files can now be found in same directory as orginal excel files
# conversion will take 15-20 seconds 