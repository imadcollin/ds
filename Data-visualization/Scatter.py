#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(40, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')

x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)
colr = np.random.rand(10)
plt.scatter(x, y, s=z * 1000, c=colr)
plt.show()
# %%
