import pandas as pd

df = pd.read_csv('matches.csv', usecols=["player_of_match"])

count = df["player_of_match"].value_counts()

print(count[count>3].to_string())