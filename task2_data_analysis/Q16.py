import pandas as pd

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print(f"Total number of runs scored by each batsman (top 10) are: \n{deliveries.groupby('batsman')['total_runs'].sum().sort_values(ascending = False).head(10)}")