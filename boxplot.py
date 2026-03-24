import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("titanic.xlsx")

plt.boxplot(df['Fare'].dropna())

plt.xlabel('Fare')
plt.title('Box Plot of Passenger Fare')

plt.show() 