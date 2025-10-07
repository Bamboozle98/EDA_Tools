from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np
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

for col in ['X1','X2','X3','X4','X5','X6']:
    table = pd.crosstab(df[col], df['Y'])
    chi2, p, dof, ex = chi2_contingency(table)
    print(col, f'p-value: {p:.4f}')


for col in ['X1','X2','X3','X4','X5','X6']:
    table = pd.crosstab(df[col], df['Y'])
    chi2, p, dof, ex = chi2_contingency(table)
    n = table.sum().sum()
    cramer_v = np.sqrt(chi2 / (n * (min(table.shape)-1)))
    print(f"{col}: p={p:.4f}, Cramer's V={cramer_v:.3f}")



sns.heatmap(pd.crosstab(df['X1'], df['Y'], normalize='index'), annot=True, cmap='Blues')
plt.title('Happiness vs Delivery Time')
plt.show()
