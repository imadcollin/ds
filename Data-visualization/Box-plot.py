#%%
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
print(df)
df.plot.box(grid="True")
# %%
