#%%
from collections import Counter

file = ('Data-processing/text.txt')

with open(file) as f:
    ln = f.readlines()
    print(ln)

    while ln:
        count = 1
        print("{}: {}".format(count, ln))
        ln = f.readline()
        count += 1

# %%
with open(file) as f:
    c = Counter(f.read().split())
    print(c)

# %%
