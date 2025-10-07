import pandas as pd

# Load the dataset (replace with your actual path)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Strip any extra spaces in column names (just in case)
df.columns = df.columns.str.strip()

# List of continuous features (replace these with actual continuous columns in your dataset)
continuous_features = ['Calcium', 'Calories', 'Carbs', 'Cholesterol', 'Copper', 'Fats', 'Fiber', 'Iron', 'Magnesium', 'Protein']  # Example continuous features

# Filter the dataframe to include only continuous columns
continuous_df = df[continuous_features]

# Compute the covariance matrix
covariance_matrix = continuous_df.cov()

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

# Print the covariance matrix
print("Covariance Matrix:")
print(covariance_matrix)

# Reset display options to defaults (optional)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
