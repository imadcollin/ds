#%%
import pandas as pd

data = pd.read_csv("Data-processing/data.csv")
print(data)
print("------Print row----")
print(data[0:5]["salary"])

print("------Print Col----")
print(data.loc[0:5, ["salary", "name"]])

print("------Print Row + Col----")
print(data.loc[[1, 2, 3], ["salary", "name"]])
# %%
