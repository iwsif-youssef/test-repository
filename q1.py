import pandas as pd
import numpy as np
import crime_data as cd

vdf = cd.ValTest_df
def normaldistribution(x, mean, var):
    return (1 / np.sqrt(2 * np.pi * var)) * np.exp(-0.5 * ((x - mean) ** 2) / var)

print(vdf["hour_float"])
