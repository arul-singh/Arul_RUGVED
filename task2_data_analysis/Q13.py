import pandas as pd

df = pd.read_csv('matches.csv', usecols=['city','umpire1', 'umpire2','umpire3'])


umpire1_max =next(city for city, count in (df['umpire1'].value_counts()).items() if count == df['umpire1'].value_counts().max())
umpire2_max =next(city for city, count in (df['umpire2'].value_counts()).items() if count == df['umpire2'].value_counts().max())
umpire3_max =next(city for city, count in (df['umpire3'].value_counts()).items() if count == df['umpire3'].value_counts().max())

print(f"The umpires who umpired the most number of matches are: '{umpire1_max}' as 1st umpire, '{umpire2_max}' as 2nd umpire and '{umpire3_max}' as the 3rd umpire")

