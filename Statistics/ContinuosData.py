import pandas as pd

# Load the dataset (replace with your actual path)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Strip any extra spaces in column names (just in case)
df.columns = df.columns.str.strip()

# Select continuous features (manually adjust this list based on your dataset)
continuous_features = ['Calories', 'Protein', 'Fats', 'Carbs', 'Fiber', 'Cholesterol', 'Magnesium', 'Calcium', 'Iron', 'Copper']

# Initialize a list to hold the report rows
report_rows = []

# Generate the report
for feature in continuous_features:
    count = df[feature].count()
    mean = df[feature].mean()
    median = df[feature].median()
    std_dev = df[feature].std()
    min_val = df[feature].min()
    max_val = df[feature].max()
    percentiles = df[feature].quantile([0.25, 0.5, 0.75])
    missing_values = df[feature].isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    cardinality = df[feature].nunique()  # Calculate cardinality

    # Append a dictionary of the results to the list
    report_rows.append({
        'Feature': feature,
        'Count': count,
        'Mean': mean,
        'Median': median,
        'Std Dev': std_dev,
        'Min': min_val,
        'Max': max_val,
        '25th Percentile': percentiles[0.25],
        '50th Percentile': percentiles[0.5],
        '75th Percentile': percentiles[0.75],
        'Missing Values': missing_values,
        'Missing %': missing_percent,
        'Card': cardinality  # Add cardinality to the report
    })

# Create a DataFrame from the list of report rows
data_quality_report = pd.DataFrame(report_rows)

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Prevent line wrapping
pd.set_option('display.max_colwidth', None)  # Prevent column truncation

# Display the data quality report
print(data_quality_report)

