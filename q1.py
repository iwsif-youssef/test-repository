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

plt.show()
data = vdf["hour_float"].to_numpy()

mu = np.mean(data)
sigma = np.std(data)
x = np.linspace(data.min(), data.max(), 200)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * \
      np.exp(-(x - mu)**2 / (2 * sigma**2))

plt.hist(data, bins=100, density=True)
plt.plot(x, pdf)
plt.title("Gaussian fit: N(μ, σ²)")
plt.xlabel("Score")
plt.ylabel("Density")
plt.show()

plt.tight_layout()


