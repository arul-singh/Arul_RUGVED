import pandas as pd

df1 = pd.read_csv('deliveries.csv')
df2 = pd.read_csv('matches.csv')

print(df1.head(1).to_string())

print(df2.head(1).to_string())