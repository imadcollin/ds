#%%
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6, 7]])
print(a)

# %%
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)

# %%
a = np.array([1, 2, 3, 4, 5], dtype=complex)
print(a)

# %%
import pandas as pd
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

#%%
data = {'Name': ['A', 'B', 'C', 'D'], 'Age': [10, 20, 40, 50]}
df = pd.DataFrame(data, index=['1', '2', '3', '4'])
print(df)
# %%
