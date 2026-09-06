#4. Tally the toss decisions each team has taken.

import pandas as pd

df = pd.read_csv('matches.csv')

tally = df.groupby(["toss_winner", "toss_decision"]).size()
print(tally)

