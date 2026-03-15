import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
sns.scatterplot(x='sepal_length', y='sepal_width', data=df)
plt.show()
df['sepal_length'].hist()
plt.show()
sns.boxplot(x=df['sepal_length'])
plt.show()
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.show()

