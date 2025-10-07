import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

# Load the dataset
df = pd.read_csv('../Data/ACME-HappinessSurvey2020.csv')

# Dictionary of Column Names and their meanings
col_def = {'Y':"Customer Happiness (0 or 1)", 'X1':"Satisfaction with Delivery Time (1-5)",
           'X2': "Satisfaction with Contents of Delivery (1-5)", 'X3': "Satisfaction with All Items Ordered (1-5)",
           'X4': "Satisfaction with Price of Order (1-5)", 'X5': "Satisfaction with Order Courier",
           'X6': "Satisfaction with Ease of Ordering on App (1-5)"}

# Select numeric columns
numeric_columns = df.select_dtypes(include=['number']).columns

output_folder = 'ChartsGraphs/Barplot'
os.makedirs(output_folder, exist_ok=True)

# Generate histograms for numeric columns
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    plt.hist(df[column].dropna(), bins=6, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {col_def[column]}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # makes tick labels integers
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))      # max 10 y-ticks

    save_path = os.path.join(output_folder, f'{col_def[column]}_barplot.png')
    plt.savefig(save_path, bbox_inches='tight')  # trims extra whitespace
    plt.close()
