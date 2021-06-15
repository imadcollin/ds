#%%
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 200)

plt.plot(bins,
         1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 /
                                                   (2 * sigma**2)),
         linewidth=3,
         color='y')
plt.show()
# %%
