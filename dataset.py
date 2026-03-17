import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("titanic.xlsx")

print("Dataset Preview:\n", df.head())

missing_values = df.isnull().sum()

missing_table = pd.DataFrame({
    'Column Name': missing_values.index,
    'Missing Values': missing_values.values
})

print("\nMissing Values Table:\n")
print(missing_table)

numeric_cols = df.select_dtypes(include=[np.number])

outliers_dict = {}

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    outliers_dict[col] = len(outliers)

outlier_table = pd.DataFrame({
    'Column': outliers_dict.keys(),
    'Outlier Count': outliers_dict.values()
})

print("\nOutlier Table:\n")
print(outlier_table)

survival_counts = df['Survived'].value_counts()

plt.figure()
survival_counts.plot(kind='bar')
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

gender_counts = df['Sex'].value_counts()

plt.figure()
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")  
plt.show()

sorted_age = df['Age'].sort_values()

plt.figure()
plt.step(range(len(sorted_age)), sorted_age)
plt.title("Step Chart of Age")
plt.xlabel("Index")
plt.ylabel("Age")
plt.show()
