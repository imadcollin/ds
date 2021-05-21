#%%
import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'subject': ['sub1', 'sub2', 'sub3', 'sub4']
})

right = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['E', 'F', 'G', 'H'],
    'subject': ['sub1', 'sub2', 'sub3', 'sub4']
})
print('---------Left-------')
print(left)
print('---------Right-------')

print(right)

groupby = left.groupby('subject')
print('--------Sub1-----')
print(groupby.get_group('sub1'))
print('-----Concatenating----')
print(pd.concat([left, right]))
# %%
