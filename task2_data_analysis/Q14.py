import pandas as pd

df = pd.read_csv('matches.csv')

print(df['season'].value_counts().sort_index(ascending=False))