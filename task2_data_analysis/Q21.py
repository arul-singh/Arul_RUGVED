#21. Find the distribution of the teams who won the matches.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('matches.csv')

labels = list(df['winner'].value_counts().to_dict().keys())
values = list(df['winner'].value_counts().to_dict().values())



fig, ax  = plt.subplots(figsize=(10, 12))


bars = ax.bar(labels, values,  color='orange', edgecolor = 'black')

ax.bar_label(bars, fontsize = 10)
ax.set_xlabel('Teams', fontsize = 15, fontweight="bold")
ax.set_ylabel('Wins',fontsize = 15, fontweight="bold")
ax.grid(axis="y", linestyle="--", alpha=0.5)
ax.tick_params(axis="x", rotation=90, labelsize = 5)
ax.set_title('Number of wins per team', fontsize = 25, fontweight = 700)

plt.show()