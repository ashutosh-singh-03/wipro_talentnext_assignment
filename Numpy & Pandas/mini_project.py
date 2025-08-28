import numpy as np
import pandas as pd

# Reading the CSV File
df = pd.read_csv('datasetExample.csv')
print("\nLoaded DataFrame:")
print(df.head())

# Detection of Outliers using IQR method
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_detected = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
print("\nDetected outliers:")
print(outliers_detected)