#15. Find total runs scored in each season.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv', usecols=['match_id', 'total_runs'])
matches = pd.read_csv('matches.csv', usecols=['id', 'season'])

merged_df = deliveries.merge(matches, left_on='match_id', right_on='id')

total_runs = merged_df.groupby('season')['total_runs'].sum().sort_index(ascending=False)

print(f"Total runs scored in each season are: \n {total_runs}")