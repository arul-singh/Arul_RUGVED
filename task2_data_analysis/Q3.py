#3. Find total count of matches city-wise.

import pandas as pd

df = pd.read_csv('matches.csv')

print(f"Counts of matches city wise: \n {df['city'].value_counts()}")
