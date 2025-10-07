import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MaxNLocator
import numpy as np

# Load dataset
df = pd.read_csv('../Data/ACME-HappinessSurvey2020.csv')

col_def = {
    'Y': "Customer Happiness (0 or 1)",
    'X1': "Satisfaction with Delivery Time (1-5)",
    'X2': "Satisfaction with Contents of Delivery (1-5)",
    'X3': "Satisfaction with All Items Ordered (1-5)",
    'X4': "Satisfaction with Price of Order (1-5)",
    'X5': "Satisfaction with Order Courier",
    'X6': "Satisfaction with Ease of Ordering on App (1-5)"
}

continuous_columns = df.select_dtypes(include=['float64', 'int64']).columns

output_folder = 'ChartsGraphs/Histograms'
os.makedirs(output_folder, exist_ok=True)

for column in continuous_columns:
    plt.figure(figsize=(7, 4.5))  # slightly smaller figure for compactness

    data = df[column].dropna()
    min_val, max_val = int(data.min()), int(data.max())

    # Align bins exactly to integers (one bin per integer)
    bins = np.arange(min_val - 0.5, max_val + 1.5, 1)

    # Perfectly touching bars — remove rwidth
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black')

    plt.title(f'Histogram of {col_def.get(column, column)}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))

    save_path = os.path.join(output_folder, f'{col_def[column]}_histogram.png')
    plt.savefig(save_path, bbox_inches='tight')  # trims extra whitespace
    plt.close()
