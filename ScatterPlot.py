import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("titanic.xlsx")

data = df[['Age', 'Fare']].dropna()

x = data['Age']
y = data['Fare']

y = y + np.random.normal(0, 5, len(y))

x = np.append(x, 5)     
y = np.append(y, 300)

plt.scatter(x, y)

plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatter Plot of Age vs Fare with Outlier')

plt.show() 