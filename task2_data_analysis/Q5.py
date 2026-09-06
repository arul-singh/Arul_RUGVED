#5. Count the total number of normal and tied matches.

import pandas as pd

df = pd.read_csv('matches.csv' , usecols=['toss_decision','toss_winner'])

print(f'Total number of normal matches is {df[df['result']!='tie'].size} and tied matches are {df[df['result']=='tie'].size}' )