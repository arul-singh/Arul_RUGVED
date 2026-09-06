import pandas as pd

df = pd.read_csv('matches.csv')

print(df.groupby('season'))