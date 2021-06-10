#%%
import pandas as pd
import numpy as np

data = {
    'Names': pd.Series(['Alice', 'Boo', 'eva', 'Alex', 'Starm']),
    'Ages': pd.Series([22, 32, 45, 55, 62]),
    'Salaries': pd.Series([1500, 1800, 2200, 4000, 6500])
}
df = pd.DataFrame(data)
print(df)
print('Media-----', df.median())
print('Mean-----', df.mean())
print('Mode-----', df.mode())
print('Deviasion-----', df.std())
print('Skewness-----\n', df.skew())
# %%
