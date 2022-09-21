from asyncore import read
import pandas as pd



df = pd.read_csv(r"Sample DataSets\test.csv")
print(df.head())