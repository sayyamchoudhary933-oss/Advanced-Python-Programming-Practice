import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Sample customer data for Exploratory Data Analysis
data = {
    "Age": [24, 27, 22, 32, 29, 25, 30, 100],
    "Monthly_Charges": [500, 600, 520, 580, 620, 550, 600, 6000],
    "Churn": ["No", "Yes", "No", "No", "Yes", "No", "Yes", "Yes"]
}
df = pd.DataFrame(data)

# Descriptive statistics
print("CUSTOMER DATASET")
print(df)
print("\nDESCRIPTIVE STATISTICS")
print(df[["Age", "Monthly_Charges"]].describe())
print("Mean Age:", df["Age"].mean())
print("Median Age:", df["Age"].median())
print("Mode Age:", df["Age"].mode()[0])

# Check and handle missing values
print("\nMISSING VALUES")
print(df.isnull().sum())
df[["Age", "Monthly_Charges"]] = df[["Age", "Monthly_Charges"]].fillna(
    df[["Age", "Monthly_Charges"]].median())

# Detect outliers using Z-score
df["Age_Zscore"] = zscore(df["Age"])
df["Charges_Zscore"] = zscore(df["Monthly_Charges"])
outliers = df[(df["Age_Zscore"].abs() > 2) |
              (df["Charges_Zscore"].abs() > 2)]

print("\nOUTLIERS (Z-score > 2)")
print(outliers[["Age", "Monthly_Charges"]])

# Visualizations
plt.figure(figsize=(6, 4))
sns.histplot(df["Age"], bins=5, kde=True)
plt.title("Age Distribution")
plt.tight_layout()
plt.savefig("age_distribution.png", dpi=150)

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Monthly_Charges"])
plt.title("Monthly Charges - Box Plot")
plt.tight_layout()
plt.savefig("charges_boxplot.png", dpi=150)
