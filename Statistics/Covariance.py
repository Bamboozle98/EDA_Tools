import pandas as pd

# Load the dataset
df = pd.read_csv('../Data/ACME-HappinessSurvey2020.csv')

# Compute variance for each numerical column
variances = df[['X1','X2','X3','X4','X5','X6']].var()
print(variances)

# Create a Covariance Matrix for all non-target features.
cov_matrix = df[['X1','X2','X3','X4','X5','X6']].cov()
print(cov_matrix)
