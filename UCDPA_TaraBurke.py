import pandas as pd
cso = pd.read_csv(r'C:\Users\tarab_000\Documents\Data Analytics CSV\RSM05.20220603T150653.csv')
print(cso)

print(cso[['Month','UNIT']])

print(cso[0:5][['Month','UNIT']])

print(cso.iloc[[1,10],[1,2]])

print(cso.iloc[0:5,0:4])

print(cso[cso['VALUE']>181.5])
print(cso.drop_duplicates(subset=['Month']).head())

print(cso.isnull())

print(cso.isnull())

print(cso.shape[0])

value_mean = cso['VALUE'].mean()
print(value_mean)

value_median = cso['VALUE'].median()
print(value_median)

print(cso.groupby('NACE Group').mean())

print(cso.groupby('NACE Group').agg(['mean','median']))

import matplotlib.pyplot as plt
import seaborn as sns

print(cso.dtypes)
sns.scatterplot(data=cso, x='Month', y='VALUE')
plt.show()

sns.scatterplot(data=cso, x='Month', y='VALUE', hue='NACE Group')
plt.show()

cso.groupby('NACE Group').mean()['VALUE'].plot.bar()
plt.show()



















