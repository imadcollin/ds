
#%%
import pandas as pd 
import Cartopy as ccrs    # Not Installed for some reason 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,15))
ax= fig._add_subplot(1,1,1, projection= ccrs.PlateCarre())
ax.set_extent(60,150,50,60)
ax.stock_img(); 
ax.coastlines()
ax.tissot(facecoler="red", alpha=0.8)
plt.show()
# %%
