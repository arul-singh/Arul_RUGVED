#2. Find the cities where the maximum and minimum number of matches were conducted.


import pandas as pd

df = pd.read_csv('matches.csv', usecols=['city'])

max_city =next(city for city, count in (df['city'].value_counts()).items() if count == df['city'].value_counts().max())
min_city =next(city for city, count in (df['city'].value_counts()).items() if count == df['city'].value_counts().min())

print(f"The city with the maximum matches is {max_city} and city with minimum matches is {min_city}")

