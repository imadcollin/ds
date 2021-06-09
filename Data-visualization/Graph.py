#%%
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

data = np.array([[1, 0, 0], [2, 0, 0], [0, 1, 1]])
mask = np.ma.masked_values(data, 0)
data = csr_matrix(data)
print(data)
print(data.data)
# %%
