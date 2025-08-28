import pandas as pd

# Program 1 Cars Dataset
cars = pd.read_csv("dataset/cars.csv")
# Inspect the first 10 Rows
print("First 10 rows:")
print(cars.head(10))

# Inspect the DataFrame by printing 'cars'
print("\nFull DataFrame:")
print(cars)

# Inspect the last 5 Rows
print("\nLast 5 rows:")
print(cars.tail(5))

# Get some meta information on our DataFrame
print("\nMeta information:")
print(cars.info())

# ====================================================================

# Program 2 50 Startups Dataset
startups = pd.read_csv("dataset/50_Startups.csv")
print(startups.head())

# Statistical summary
print("\nStatistical summary:")
print(startups.describe())

# Correlation coefficients between dependent and independent variables
print("\nCorrelation coefficients with Profit:")
print(startups.corr(numeric_only=True)['Profit'])