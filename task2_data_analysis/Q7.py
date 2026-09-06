#7. Find the team which won the match by the highest and lowest number of runs

import pandas as pd

df = pd.read_csv("matches.csv")

subset=sorted(df['win_by_runs'].to_list())
subset.reverse()


print(subset)
