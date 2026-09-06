#12. Compute the average runs scored in matches in all the venues.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv', usecols=['match_id', 'total_runs'])
matches = pd.read_csv('matches.csv', usecols=['id', 'venue'])

merged_df = deliveries.merge(matches, right_on='id', left_on='match_id')

merged_df = merged_df.groupby(['venue', 'match_id'])['total_runs'].sum().groupby('venue').mean().round(2).reset_index()

print(merged_df)

