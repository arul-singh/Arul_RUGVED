#8. Calculate mean, median and standard deviation of ‘win_by_runs'

import pandas as pd

df = pd.read_csv('matches.csv' , usecols=['win_by_runs'])

print(f'The mean = {df.mean()['win_by_runs']}, median = {df.median()['win_by_runs']} and the mode = {df.mode()['win_by_runs'].to_list()[0]}')



