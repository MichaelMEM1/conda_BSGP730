import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

def CFOF1(csv_file):
    #Extract the filename with and without extension
    csv_filename = os.path.basename(csv_file)
    csv_title = os.path.splitext(csv_filename)[0]  # Get filename without extension

    #Reading the csv file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # Ensure 'Cell ID' is treated as a categorical variable (to give distnct colors to each Cell ID)
    df['Cell ID'] = pd.Categorical(df['Cell ID'])

    # Boxplot to check for outliers in the 'Intracellular Calcium' column for the 'Fura_' columns
    plt.figure(figsize=(10, 6))

    # Create the boxplot
    sns.boxplot(data=df, x='Cell ID', y='Intracellular Calcium', width=0.5, fliersize=3, palette="Set1", hue='Cell ID')

    # Add a title to the plot
    plt.title(f'Outlier Check for Intracellular Calcium - {csv_title}')

    # Save the plot as a PNG file
    plt.savefig('OutlierCheck.png')

    # Show the plot
    plt.show()