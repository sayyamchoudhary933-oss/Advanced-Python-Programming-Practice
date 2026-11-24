import pandas as pd
import numpy as np

# Create a Pandas Series with ten random numbers
np.random.seed(10)
series = pd.Series(np.random.randint(10, 100, 10))
print("PANDAS SERIES")
print(series)

# Create a DataFrame
data = {
    "Name": ["Amit", "Riya", "Rahul", "Neha", "Amit"],
    "Age": [20, 21, np.nan, 22, 20],
    "Marks": [85, 90, 78, np.nan, 85]
}
df = pd.DataFrame(data)
print("\nORIGINAL DATAFRAME")
print(df)

# Indexing and selecting data
print("\nSELECTED COLUMN: Name")
print(df['Name'])
print("\nFIRST TWO ROWS")
print(df.iloc[0:2])

# Data cleaning: fill missing values and remove duplicates
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df = df.drop_duplicates()
print("\nCLEANED DATAFRAME")
print(df)

# Merge two DataFrames using a common column
dept = pd.DataFrame({
    "Name": ["Amit", "Riya", "Rahul", "Neha"],
    "Department": ["IT", "HR", "IT", "Sales"]
})
merged = pd.merge(df, dept, on='Name', how='left')
print("\nMERGED DATAFRAME")
print(merged)

# Grouping and aggregation
print('\nAVERAGE MARKS BY DEPARTMENT')
print(merged.groupby('Department')['Marks'].mean())
