import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Load the dataset
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Select continuous columns
continuous_columns = df.select_dtypes(include=['float64', 'int64'])

# Generate the scatterplot matrix
scatter_matrix(continuous_columns, figsize=(12, 12), color='skyblue', marker='o', hist_kwds={'bins': 30})
plt.show()
