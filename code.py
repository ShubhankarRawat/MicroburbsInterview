import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("input.csv")

print(df.shape)
df.head()

## filling null values
df['Westpac: 4 year forecast'].fillna(df["Westpac: 4 year forecast"].median())
df['Harry Spent: 5 year forecast'].fillna(df["Harry Spent: 5 year forecast"].median())

df.describe() #to get the mean and median of all forecasters

