#10. Find the players who have won ‘Player of the Match’ more than 3 times.

import pandas as pd

df = pd.read_csv('matches.csv', usecols=["player_of_match"])

count = df["player_of_match"].value_counts()

print(count[count>3].to_string())