import pandas as pd

deliveries = pd.read_csv('deliveries.csv')


wickets_taken_bool = deliveries['dismissal_kind'].isin(['caught', 'bowled','lbw', 'caught and bowled', 'stumped','hit wicket',])

print(deliveries.sample().to_string())
wicket_count = (wickets_taken_bool.groupby('bowler')['dismissal_kind'].count())