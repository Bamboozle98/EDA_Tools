import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MaxNLocator


# Load the dataset (replace with the path to your dataset)
df = pd.read_csv('../Data/ACME-HappinessSurvey2020.csv')

output_folder = 'ChartsGraphs/HeatMap'
os.makedirs(output_folder, exist_ok=True)

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

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heat Map of Target and Independent Variables')


save_path = os.path.join(output_folder, f'heat_map.png')
plt.savefig(save_path, bbox_inches='tight')  # trims extra whitespace
plt.close()