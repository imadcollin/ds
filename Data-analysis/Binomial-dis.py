#%%
from matplotlib.pyplot import xlabel, ylabel
from numpy.core.fromnumeric import size
from scipy.stats import binom, kde
import seaborn as sb

binom.rvs(size=10, n =20, p = 0.8)
binom_data=binom.rvs(size=1000, p=0.8,loc=0, n=20)
ax=sb.displot(binom_data, color='green', kde=True)
ax.set(xlabel="xlable", ylabel="ylabel")
# %%
