#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = x * x
plt.title("Sample")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y)
plt.plot(x, y, "red")
plt.plot(x, y, ">")
#plt.savefig("sample.pdf", format="pdf")
# %%
