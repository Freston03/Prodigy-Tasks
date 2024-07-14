import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("F:\\HR\\US_Accidents.csv")
print(df.head(5))
print(df.tail())
print(df.columns)
print(df.describe)
print(df.info)
print(df.isnull().sum())
print(df.duplicated().sum())

print(df.City.unique())

accident_in_cities = df.City.value_counts()
print(accident_in_cities[:30])
plt.figure(figsize=(10,6))
accident_in_cities[:30].plot(kind='barh')
plt.title('Top 30 Cities with Most Accidents')
plt.xlabel('City')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10,10))
accident_in_cities[:25].plot(kind = 'pie',autopct = '%1.1f%%',startangle = 140)
plt.title('Top 25 Cities with Most Accidents')
plt.show()


plt.figure(figsize=(10,6))
sns.histplot(accident_in_cities[:25],kde = True,bins=30)
plt.title('Top 25 Cities with Most Accidents')
plt.show()

plt.figure(figsize=(15,10))
sns.scatterplot(y=df.Start_Lat, x=df.Start_Lng,hue= df.State)
plt.show()

