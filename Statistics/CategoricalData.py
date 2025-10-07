import pandas as pd

# Load the dataset (replace with your actual path)
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Strip any extra spaces in column names (just in case)
df.columns = df.columns.str.strip()

# Select categorical features (adjust this list based on your dataset)
categorical_features = ['Category Name', 'Food Name']  # Replace with your categorical columns

# Initialize a list to hold the report rows
categorical_report_rows = []

# Generate the report
for feature in categorical_features:
    count = df[feature].count()
    unique_values = df[feature].nunique()
    missing_values = df[feature].isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    cardinality = unique_values

    # Mode and second mode
    mode_series = df[feature].value_counts()
    mode = mode_series.index[0] if not mode_series.empty else None
    mode_freq = mode_series.iloc[0] if not mode_series.empty else 0

    # Second mode
    second_mode = mode_series.index[1] if len(mode_series) > 1 else None
    second_mode_freq = mode_series.iloc[1] if len(mode_series) > 1 else 0

    # Append a dictionary of the results to the list
    categorical_report_rows.append({
        'Feature': feature,
        'Count': count,
        'Missing Values': missing_values,
        'Card': cardinality,
        'Mode': mode,
        'Mode Freq.': mode_freq,
        '2nd Mode': second_mode,
        '2nd Mode Freq.': second_mode_freq
    })

# Create a DataFrame from the list of report rows
categorical_data_quality_report = pd.DataFrame(categorical_report_rows)

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Prevent line wrapping
pd.set_option('display.max_colwidth', None)  # Prevent column truncation

# Display the data quality report for categorical features
print(categorical_data_quality_report)

