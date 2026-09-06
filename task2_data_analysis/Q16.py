#16. Calculate total number of runs scored by each batsman and display top 10.

import pandas as pd

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

total_runs = deliveries.groupby('batsman')['total_runs'].sum().sort_values(ascending = False).head(10)

print(f"Total number of runs scored by each batsman (top 10) are: \n{total_runs}")