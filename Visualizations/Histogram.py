# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset (replace with the path to your dataset)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Select continuous (numerical) columns
# You can use df.select_dtypes to automatically select numerical columns
continuous_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Create a folder to save the histograms
output_folder = 'ChartsGraphs/Histograms'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Generate and save histograms
for column in continuous_columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df[column].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)

    # Save the plot in the designated folder
    save_path = os.path.join(output_folder, f'{column}_histogram.png')
    plt.savefig(save_path)  # Save each figure as a PNG file
