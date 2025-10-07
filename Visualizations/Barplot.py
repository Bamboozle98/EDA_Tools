import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../Data/food/foodstruct_nutritional_facts_modified.csv')

# Select categorical columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns

# Generate barplots using matplotlib
for column in categorical_columns:
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(f'Barplot of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.show()
