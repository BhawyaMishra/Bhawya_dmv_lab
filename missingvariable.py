import pandas as pd
import numpy as np

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Aman", "Riya", "John", "Sara", "Raj"],
    "Age": [21, np.nan, 20, 22, np.nan],
    "Salary": [30000, 35000, np.nan, 40000, 38000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print("\nDataset after Handling Missing Values:")
print(df)

print("\nMissing Values After Treatment:")
print(df.isnull().sum())
