import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("F:\\HR\\distribution_population.csv.csv")

print(df.head())
print(df.tail())
print(df.columns)
print(df.describe)
print(df.shape)
print(df.info)

df_attr = df.drop(['Country Code' , 'Indicator Name' , 'Indicator Code'],axis=1)

country_chosen = 'India'

country_data = df_attr[df_attr['Country Name'] == country_chosen]
years = country_data.columns[2:].astype(int)
population = country_data.iloc[:, 2:].values.flatten()

# Scatter Plot
plt.figure(figsize=(5, 3))
plt.scatter(years, population, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population of {country_chosen} Over the Years')
plt.xticks(rotation=45)  # Rotate x-axis labels if necessary
plt.tight_layout()  # Adjust layout for better fit
plt.show()

# Pie Chart
population_pie = population[-5:]  # Last 5 years
years_pie = years[-5:]

plt.figure(figsize=(5, 5))
plt.pie(population_pie, labels=years_pie, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title(f'Population Distribution of {country_chosen} (Last 5 Years)')
plt.tight_layout()  # Adjust layout for better fit
plt.show()

#Column Chart

plt.figure(figsize=(5, 3))
plt.bar(years, population, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population of {country_chosen} Over the Years')
plt.xticks(rotation=45)  # Rotate x-axis labels if necessary
plt.tight_layout()  # Adjust layout for better fit
plt.show()