#%%
from sqlalchemy import create_engine
import pandas as pd
from pandas.io import sql

print("------Read------")
data = pd.read_csv('data.csv')
engine = create_engine('sqlite:///:memory:')

data.to_sql('myTable', engine)

myData = pd.read_sql_query('SELECT * FROM myTable', engine)
print('Result 1')
print(myData)
print('')
# %%
print("------Insert------")
sql.execute('INSERT INTO myTable VALUES(?,?,?,?,?,?)',
            engine,
            params=[('id', 9, 'Ruby', 711.20, '2015-03-27', 'IT')])
myData = pd.read_sql_query('SELECT * FROM myTable', engine)

print(myData)
# %%
print("------Delete------")
sql.execute('DELETE FROM myTable WHERE name=(?)', engine, params=[('Ruby')])
myData = pd.read_sql_query('SELECT * FROM myTable', engine)

print(myData)
# %%
