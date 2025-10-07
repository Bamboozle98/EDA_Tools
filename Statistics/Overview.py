import pandas as pd
import numpy

# Load dataset
df = pd.read_csv('../Data/ACME-HappinessSurvey2020.csv')

col_def = {
    'Y': "Customer Happiness (0 or 1)",
    'X1': "Satisfaction with Delivery Time (1-5)",
    'X2': "Satisfaction with Contents of Delivery (1-5)",
    'X3': "Satisfaction with All Items Ordered (1-5)",
    'X4': "Satisfaction with Price of Order (1-5)",
    'X5': "Satisfaction with Order Courier",
    'X6': "Satisfaction with Ease of Ordering on App (1-5)"
}

# Get an overview of the dataset and automatically check for Null values.
df.describe()
df.info()
df.isna().sum()
