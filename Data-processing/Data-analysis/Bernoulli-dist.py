#%%
from scipy.stats import bernoulli
import seaborn as sb

binom_data = bernoulli.rvs(p=0.4, size=1000)
ax = sb.displot(binom_data, kde=True, color="green")
ax.set(xlabel="xlabel", ylabel="ylabel")
# %%
