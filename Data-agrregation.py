#%%
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2010', periods=10),
                  columns=['A', 'B', 'C', 'D'])

print(df)
print('-------Aggregate sum------')
r = df.rolling(window=3, min_periods=1)
print(r['A'].aggregate(np.sum))
print('-------Aggregate sum of multi col------')
print(r['A', 'B'].aggregate(np.sum))

# %%
