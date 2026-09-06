#9. Find the venue where the team won by the highest and lowest number of run
import pandas as pd

df = pd.read_csv('matches.csv', usecols=['id','venue', 'win_by_runs'])

filter = df[df['win_by_runs']>0]


print(f'The venue where the team won by the highest is "{filter.max()['venue']}" and the where team won by minimum runs is "{filter.min()['venue']}"')

