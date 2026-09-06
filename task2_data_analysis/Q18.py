#18. Compute batting averages and display top 10.

import pandas as pd

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

total_runs = deliveries.groupby('batsman')['batsman_runs'].sum()
total_outs = deliveries['player_dismissed'].value_counts()

averages = (total_runs/total_outs).dropna().sort_values(ascending=False).round(2).head(10)

print(averages)