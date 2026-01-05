import pandas as pd
import numpy as np
import crime_data as cd
import matplotlib.pyplot as plt

vdf = cd.ValTest_df

fig, axs = plt.subplots(2, 2)

axs[0, 0].hist(vdf["hour_float"], bins=24, density=True)
axs[0, 0].set_title("hours")

axs[0, 1].hist(vdf["latitude"], bins=30, density=True)
axs[0, 1].set_title("latitude")

axs[1, 0].hist(vdf["longitude"], bins=30, density=True)
axs[1, 0].set_title("longitude")

axs[1, 1].hist(vdf["victim_age"], bins=30, density=True)
axs[1, 1].set_title("ictim age")

plt.tight_layout()

plt.show()
