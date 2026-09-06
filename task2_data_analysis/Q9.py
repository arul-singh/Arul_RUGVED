from random import sample

import pandas as pd

df = pd.read_csv('matches.csv', usecols=['win_by_runs', 'venue', 'winner'])

print(df['win_by_runs'].)
