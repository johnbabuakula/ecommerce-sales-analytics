
import pandas as pd

# Read our sales dataset
df = pd.read_csv("data/raw/sales_data.csv")

# Display the dataset
print(df)


# First five rows
print("FIRST FIVE ROWS")
print(df.head())

# Last five rows
print("LAST FIVE ROWS")
print(df.tail())

# Number of rows and columns
print("DATASET SHAPE")
print(df.shape)

# Column names
print("COLUMN NAMES")
print(df.columns)

# Dataset information
print("DATASET INFORMATION")
df.info()

print(df.isnull())
print(df.isnull().count())

#removing the duplicate rows

print("Before removing duplicates:", df.shape)

df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

#fill missing values

# Fill missing customer names
df["Customer"] = df["Customer"].fillna("Unknown")

# Fill missing prices using median
df["Price"] = df["Price"].fillna(df["Price"].median())

# Fill missing cities
df["City"] = df["City"].fillna("Unknown")

# Check missing values
print(df.isnull().sum())


print(df)

df.to_csv("data/processed/cleaned_sales.csv", index=False)

print("Data cleaning completed successfully!")