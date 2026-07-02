import pandas as pd

# Load dataset
df = pd.read_csv("dataset/7817_1.csv")

# Display dataset information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Select only required columns
df = df[['name', 'brand', 'categories', 'reviews.rating']]

# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Display cleaned data
print("\nCleaned Dataset:")
print(df.head())

print("\nCleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("dataset/cleaned_dataset.csv", index=False)

print("\n✅ Cleaned dataset saved as cleaned_dataset.csv")