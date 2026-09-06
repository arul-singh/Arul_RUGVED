import pandas as pd

df = pd.read_csv('matches.csv')

count = df["player_of_match"].value_counts()

print(count[count>3].to_string())