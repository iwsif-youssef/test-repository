import numpy as np
import pandas as pd


crimes_df = pd.read_csv("crimes.csv")
split = crimes_df.iloc[:, 13]
Train_df = crimes_df[split == "TRAIN"]
Val_df = crimes_df[split == "VAL"]
Test_df = crimes_df[split == "TEST"]
ValTest_df = crimes_df[split.isin(["VAL", "TEST"])]