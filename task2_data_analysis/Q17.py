#17. Compute the total number of wickets taken by each bowler.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv', usecols=['bowler', 'dismissal_kind'])

wickets_taken_bool = deliveries['dismissal_kind'].isin(['caught', 'bowled','lbw', 'caught and bowled', 'stumped','hit wicket',])

wicket_taken_df = deliveries[wickets_taken_bool]

wicket_taken_df = wicket_taken_df.groupby('bowler')['dismissal_kind'].count().sort_values().to_string()

print(wicket_taken_df)