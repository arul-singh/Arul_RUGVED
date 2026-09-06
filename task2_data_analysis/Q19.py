import matplotlib.pyplot as plt
import pandas as pd

matches = pd.read_csv("matches.csv")

toss_counts = pd.crosstab(matches["season"], matches["toss_decision"])


toss_counts.plot(kind="bar", figsize=(12, 6), color=["#e74c3c", "#3498db"], width=0.8)

plt.title("Toss Decisions", fontsize=14, fontweight="bold")
plt.xlabel("Season", fontsize=12)
plt.ylabel("Number of Matches", fontsize=12)
plt.legend(title="Toss Decision")
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.show()