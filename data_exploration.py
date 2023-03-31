import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import tr
from pathlib import Path

df = pd.read_csv("AAPL.csv")
#df = pd.read_excel(Path("D:/Dropbox/Sync/Graduate School/Spring Semester/Alternative Investments/Assignment 1 Excel Files Draft.xlsx"))

#Explaratory Data Analysis
print(df.info())
print(df.describe())

#Converting Date Column from "object" datatype to "datetime" datatype

print(df["Date"])
print(df['Date']>"2020-01-01")
print(df[df['Date']>"2020-01-01"])
df['Date'] = pd.to_datetime(df['Date'])

plt.plot(df['Date'], df['Open'])
plt.title('Open values for AAPL')
plt.xlabel('Year')
plt.ylabel('Value')
plt.show()

#split the data

X = df.drop("Value")
Y = df["Value"]

xtrain, ytrain, xtest, ytest = train_test_split(X,Y, random_state = 42)

model = LinearRegression()

model.fit(xtrain, ytrain)

ypred = model.predict(xtrain)

plt.plot(ypred, ytest)

plt.title("Prediction v. True Data")

plt.show()