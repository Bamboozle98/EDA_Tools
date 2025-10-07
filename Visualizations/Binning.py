import pandas as pd

# Load the dataset (replace with your actual path)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Strip any extra spaces in column names (just in case)
df.columns = df.columns.str.strip()

# Check the range of Calories
min_calories = df['Calories'].min()
max_calories = df['Calories'].max()
print(f"Min Calories: {min_calories}, Max Calories: {max_calories}")

# Define custom bins for calories based on the observed range
bins_calories = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
labels_calories = range(len(bins_calories) - 1)

# Equal-Width Binning for Calories
df['Calories_Binned'] = pd.cut(df['Calories'], bins=bins_calories, labels=labels_calories, right=True)

# Print the ranges for equal-width binning
print("Equal-Width Binning Ranges for Calories:")
print(df['Calories_Binned'].value_counts())

# Equal-Frequency Binning for Protein
num_bins_protein = 4   # Define the number of bins
protein_bins = pd.qcut(df['Protein'], q=num_bins_protein, labels=False)
df['Protein_Binned'] = protein_bins

# Print the quantiles for equal-frequency binning
protein_quantiles = df['Protein'].quantile([i / num_bins_protein for i in range(num_bins_protein + 1)])
print("\nEqual-Frequency Binning Quantiles for Protein:")
print(protein_quantiles)

# Display the binned feature values
print("\nBinned Calories:\n", df[['Calories', 'Calories_Binned']].head())
print("\nBinned Protein:\n", df[['Protein', 'Protein_Binned']].head())
