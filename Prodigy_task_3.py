import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("F:\\HR\\Customer-Churn-Records.csv")
print(df.head())
print(df.head())
print(df.tail())
print(df.columns)
print(df.describe)
print(df.info)
print(df.isnull().sum())
print(df.duplicated().sum())

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import LabelEncoder

data = df.drop(['RowNumber', 'Surname', 'Geography', 'Gender', 'Card Type'], axis=1)
print(data.isnull().sum())
print(data.shape)

minimum_balance = data["Balance"].mean()
active_member = data["IsActiveMember"].mean()

def create_purchase_label(row):
    if row["IsActiveMember"] > minimum_balance and row["Balance"] > minimum_balance:
        return 1
    else:
        return 0

data['PurchaseLabel'] = data.apply(create_purchase_label, axis=1)
print(data[['Balance', 'IsActiveMember', 'PurchaseLabel']])

y = data['PurchaseLabel']
x = data.drop(['PurchaseLabel'] , axis=1)
print(x.head())
print(y.head())

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
classifier = DecisionTreeClassifier(random_state=42)

classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy is : " , accuracy)

print("Classification Report is :",classification_report(y_test,y_pred))

