#11. Find all deliveries where the batsman scored a six.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv', usecols=['total_runs', ])

print(f"Total number of sixes are : {len(deliveries[deliveries['total_runs']==6])}")
