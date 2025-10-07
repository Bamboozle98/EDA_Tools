import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (replace with the path to your dataset)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Strip any extra spaces in column names (just in case)
df.columns = df.columns.str.strip()

# Print column names to verify the correct name
print(df.columns)

# Correct column name based on your dataset (e.g., 'Food Category')
categories_of_interest = ['Meat', 'Vegetables', 'Grains']
filtered_df = df[df['Category Name'].isin(categories_of_interest)]  # Update column name here

# Plot boxplot for a continuous feature (e.g., 'calories')
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_df, x='Category Name', y='Calories', palette='Set2')  # Update column name
plt.title('Boxplot of Calories for Selected Categories')
plt.ylabel('Calories')
plt.xlabel('Food Category')
plt.show()
