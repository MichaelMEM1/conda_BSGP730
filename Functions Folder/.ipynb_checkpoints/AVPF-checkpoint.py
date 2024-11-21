import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

def AVP1(csv_file):
    # Extract the filename with and without extension
    csv_filename = os.path.basename(csv_file)
    csv_title = os.path.splitext(csv_filename)[0]  # Get filename without extension

    # Read CSV file as a pandas dataframe
    df = pd.read_csv(csv_file)

    # Creating a average data frame
    time_averages = df.groupby('Time')['Intracellular Calcium'].mean().reset_index()

    # Renaming the data values column into a average data column
    time_averages = time_averages.rename(columns={'Intracellular Calcium': 'Average Intracellular Calcium'})

    # Creating a plot of the averages

    sns.set_theme(  style ="whitegrid")
    sns.lineplot(x="Time", y="Average Intracellular Calcium",
             data=time_averages)
    plt.title('Average Calcium Transients') # Title
    plt.xlabel("Time (s)")  # Set the label for the x-axis
    plt.ylabel("Intracellular Calcium")  # Set the label for the y-axis
    # Set x-axis and y-axis limits
    plt.xlim(0, 1.2)  # For example, limit x-axis from 0 to 1.2
    plt.ylim(0,2.5)   # For example, limit y-axis from 0 to 2.5
    plt.show()