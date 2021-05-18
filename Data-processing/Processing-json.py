#%%
from numpy import record
from numpy.core import records
import pandas as pd
import json

df = pd.read_json('Data-processing/dataSet.json', orient='records')
print(df.to_string())

# with open("Data-processing/dataSet.json") as j:
#     data= json.load(j)
#     print(data)

print("------Col-----")
print(df.loc[0:5, ["Salary", "Name"]])

print("------Record-----")
print(df.to_json(orient='records', lines=True))
# %%
