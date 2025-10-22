import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta

combined_df = pd.read_csv("combined_df.csv")
combined_df["date"] = combined_df["date"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
width = np.min(np.diff(combined_df.date))/2

plt.figure(figsize=(6.5,3))
plt.bar(combined_df.date, combined_df.unique_protests, width=width*2,  color="#ffa300aa", label="HKMap protests")
plt.bar(combined_df.date, combined_df.wiki_unique_cacode_protests, width=width*2, color='#0bb4ffaa', label="News protests")
plt.xlabel("Date")
plt.ylabel("Number of protests")
plt.legend(loc="upper left", frameon=False)

plt.savefig("fig4.jpg", dpi=300, bbox_inches="tight")