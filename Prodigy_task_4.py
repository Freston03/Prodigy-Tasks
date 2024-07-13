import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

data_names = ['ID' , 'Entity' , 'Sentiment' , 'Content']
df = pd.read_csv("F:\\HR\\twitter_training.csv",names = data_names)
print(df.head())
print(df.tail())
print(df.columns)
print(df.describe)
print(df.shape)
print(df.info)

print(df.isnull().sum())
print(df.duplicated().sum())

sentiment_count = df['Sentiment'].value_counts()
print(sentiment_count)

plt.figure(figsize=(6, 3))
sentiment_count.plot(kind='pie', color = ['red' , 'green' , 'pink' , 'brown'])
plt.title('Sentiment Analysis Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()

brand_data = df[df['Entity'].str.contains('Amazon',case = False)]
brand_sentiment_counts = brand_data['Sentiment'].value_counts()
print(brand_sentiment_counts)

plt.figure(figsize=(6, 6))
plt.pie(brand_sentiment_counts, labels=brand_sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Distribution for Amazon')
plt.show()