#%%
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10)
y = x ^ 2
z = x ^ 4
t = x ^ 3

# Naming
plt.title("Sample")
plt.xlabel("X")
plt.ylabel("Y")

# Drawing
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, t)

# Annotating
plt.annotate(xy=[2, 1], s="Entry")
plt.annotate(xy=[4, 6], s="Extra")

# Legend
plt.legend(["1", "2", "3"])

# Styling
plt.style.use('fast')
plt.plot(x, z)

# %%
