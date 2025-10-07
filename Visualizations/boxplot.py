import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MaxNLocator


# Load the dataset (replace with the path to your dataset)
df = pd.read_csv('../Data/ACME-HappinessSurvey2020.csv')

# Dictionary of Column Names and their meanings
col_def = {
    'Y': "Customer Happiness (0 or 1)",
    'X1': "Satisfaction with Delivery Time (1-5)",
    'X2': "Satisfaction with Contents of Delivery (1-5)",
    'X3': "Satisfaction with All Items Ordered (1-5)",
    'X4': "Satisfaction with Price of Order (1-5)",
    'X5': "Satisfaction with Order Courier",
    'X6': "Satisfaction with Ease of Ordering on App (1-5)"
}

# Select numeric columns
numeric_columns = df.select_dtypes(include=['number']).columns

# Print column names to verify the correct name
print(df.columns)

output_folder = 'ChartsGraphs/Boxplots'
os.makedirs(output_folder, exist_ok=True)


for column in numeric_columns[1:]:
    sns.boxplot(x='Y', y=column, data=df)
    title = str(col_def[column] + ' by Happiness')
    plt.title(title)
    plt.xlabel('Customer Happiness (0 = Unhappy, 1 = Happy)')
    plt.ylabel(col_def[column])

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # makes tick labels integers
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5))      # max 10 y-ticks

    save_path = os.path.join(output_folder, f'{col_def[column]}_histogram.png')
    plt.savefig(save_path, bbox_inches='tight')  # trims extra whitespace
    plt.close()
