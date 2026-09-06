#6. Find the teams where the result was a tie.

import pandas as pd

df = pd.read_csv('matches.csv', usecols=['result', 'team1', 'team2'])

print(df.columns)
x = df[df['result']=='tie']

print(x)
print(df.groupby(x))