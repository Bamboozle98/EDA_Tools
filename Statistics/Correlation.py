import pandas as pd

# Load the dataset (replace with your actual path)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Strip any extra spaces in column names (just in case)
df.columns = df.columns.str.strip()

# List of continuous features (ensure these are all your continuous columns)
continuous_features = ['Calcium', 'Calories', 'Carbs', 'Cholesterol', 'Copper', 'Fats', 'Fiber', 'Iron', 'Magnesium', 'Protein']  # Update with your features

# Filter the dataframe to include only continuous columns
continuous_df = df[continuous_features]

# Compute the correlation matrix
correlation_matrix = continuous_df.corr()

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Reset display options to defaults (optional)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
