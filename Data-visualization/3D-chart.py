#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

chart = plt.figure()
chart3D = chart.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data(0.08)
chart3D.plot_wireframe(x, y, z, color='r', rstride=15, cstride=13)
plt.show()
# %%
