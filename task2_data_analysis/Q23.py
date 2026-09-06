#23. Visualize the top 5 teams with the most wins across all seasons.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('matches.csv')

winners = df['winner'].value_counts().head(5).to_dict()

labels = list(winners.keys())
values = list(winners.values())

fig, ax = plt.subplots(figsize = [10,6])

bars = ax.bar(labels, values, width=0.6, color='orange')
ax.set_title('Top 5 teams with the most wins', fontweight = 'bold')
ax.set_xlabel('Teams', fontsize = 10)
ax.set_ylabel('Wins',fontsize = 10, fontweight="bold")
ax.grid(axis="y", linestyle="--", alpha=0.6)
ax.tick_params(axis="x", rotation=0, labelsize = 8)
ax.bar_label(bars)
plt.ylim(0,120)

plt.show()