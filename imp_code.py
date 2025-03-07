import pandas as pd
import os

# create a sample DataFrame with column names
data = {'Name':['Alice','Bob','Charlie'],
        'Age' : [25,30,35],
        'City': ['NYC','LA','DC']}

df = pd.DataFrame(data)

# Ensure the 'data' directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Define the filepath
file_path = os.path.join(data_dir,'sample_data.csv')

# Save the dataframe to a CSV file, icluding the column name
df.to_csv(file_path,index=False)

print(f"csv file saved to : {file_path}")