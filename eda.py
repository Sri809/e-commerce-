import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_dataset.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nTop 10 Brands")
print(df['brand'].value_counts().head(10))

print("\nTop 10 Categories")
print(df['categories'].value_counts().head(10))