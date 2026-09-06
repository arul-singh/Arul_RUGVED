#1. Count the total number of matches conducted in 2008.

import pandas as pd

df = pd.read_csv('matches.csv', usecols=['season'])

print(f"Number of matches in 2008 is {len(df[df['season'] == 2008])}")


