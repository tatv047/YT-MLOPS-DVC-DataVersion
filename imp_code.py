import pandas as pd
import os

# create a sample DataFrame with column names
data = {'Name':['Alice','Bob','Charlie'],
        'Age' : [25,30,35],
        'City': ['NYC','LA','DC']}

df = pd.DataFrame(data)

# Add a new row to df for V2
new_row_loc = {'Name':'GF1','Age': 20,"City": 'City1'}
df.loc[len(df.index)] = new_row_loc

# Add a new row to df for V3
new_row_loc = {'Name':'GF2','Age': 31,"City": 'City2'}
df.loc[len(df.index)] = new_row_loc

# Ensure the 'data' directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Define the filepath
file_path = os.path.join(data_dir,'sample_data.csv')

# Save the dataframe to a CSV file, icluding the column name
df.to_csv(file_path,index=False)

print(f"csv file saved to : {file_path}")