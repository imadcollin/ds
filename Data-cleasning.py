#%%
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5, 3),
                  index=['a', 'b', 'c', 'd', 'e'],
                  columns=['1', '2', '3'])
print(df)
print("_______ReIndex______")
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(df)
print("_______Is Null______")

print(df['1'].isnull())
print("_______Fill Null______")
print(df['1'].fillna(0))
print("_______Pad______")
print(df['1'].fillna(method='pad'))

print("_______Drop Missing______")
print(df.dropna())

print("_______Replace______")
df = pd.DataFrame({'One': [1, 2, 3, 4], 'Two': [10, 20, 30, 40]})
print(df)
print("_______Replace______")
print(df.replace({1: 10, 10: 100}))
