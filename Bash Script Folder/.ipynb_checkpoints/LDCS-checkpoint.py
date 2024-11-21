import numpy as np
import pandas as pd
import os

# Making the python code executable on the first argument
if __name__ == "__main__":
    if len(sys.argv) < 2:  
        print("Usage: python csv_to_dataframe.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]  

#Extract the filename with and without extension
csv_filename = os.path.basename(csv_file)
csv_title = os.path.splitext(csv_filename)[0]  # Get filename without extension

# Read CSV file as a pandas dataframe
df = pd.read_csv(csv_file)

# Getting information on the data set (identifying column names and number of columns)
fura_columns =  [col for col in df.columns if col.startswith('Fura_')]
cell_columns = [col for col in df.columns if col.startswith('CELL')]
max_columns = len(df.columns)

# Combine both lists of columns
value_vars = fura_columns + cell_columns

# Creating a long data set
df_long = pd.melt(df, id_vars=[df.columns[0]], value_vars=value_vars, 
                       var_name='Cell ID', value_name='Intracellular Calcium')

# Convert wide data to long 
df_long.to_csv(f'{csv_title}_Long.csv', index=False)