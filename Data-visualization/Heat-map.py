#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
# df= pd.DataFrame(np.random.rand(10,3), columns=['A','B','C']);
data = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}]
index = ['1', '2', '3']
col = ['A', 'B', 'C', 'D', 'E']
df = DataFrame(data, index=index, columns=col)
plt.pcolor(df)
print(df)

# %%
