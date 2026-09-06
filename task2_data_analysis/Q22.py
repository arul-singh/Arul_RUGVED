#22. Visualize the toss outcomes of all teams.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('matches.csv')



data = pd.crosstab(df["toss_winner"], df["toss_decision"])

data.plot(kind="bar", figsize=(10, 12), color=["green", "red"], width=0.8)

plt.title("Toss Outcomes", fontsize=20, fontweight="bold")
plt.xlabel("Teams", fontsize=14, fontweight = 'bold')
plt.ylabel("Number of Matches", fontsize=15, fontweight = 'bold')
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tick_params(axis="x", rotation=75, labelsize = 5)



plt.show()