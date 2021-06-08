#%%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

data = pd.read_csv("sampel.csv")
df = pd.DataFrame(data, columns=['ValueDate', 'Price'])
print(df)

df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']

plt.plot(figsize=(15, 6))
plt.show()

# %%
