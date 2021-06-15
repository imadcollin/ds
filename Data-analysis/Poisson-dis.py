#%%
from scipy.stats import poisson 
import seaborn as sb 
binom_data= poisson.rvs(mu=4, size=1000)
ax=sb.displot(binom_data, color="green", kde=True)
ax.set(xlabel="xlabel", ylabel="ylabel")

# %%
