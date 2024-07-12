import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("F:\\CSV\\Titanic.csv")

print(df.head(5))
print(df.tail(5))
print(df.columns)
print(df.describe)
print(df.info)
print(df.isnull().sum())
print(df.duplicated().sum())

plt.figure(figsize=(6,4))
sns.histplot(df["Age"],kde=True)
plt.title("Survived Passengers")
plt.xlabel("Age of Passesgers")
plt.ylabel("Count")
plt.show()


plt.figure(figsize=(6, 3))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", loc="upper right")
plt.show()

plt.figure(figsize=(6, 3))
sns.scatterplot(data=df, x="Pclass", y="Fare", hue="Survived")
plt.title("Scatter Plot of Pclass vs Fare")
plt.xlabel("Pclass")
plt.ylabel("Fare")
plt.legend(title="Survived")
plt.show()
