#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://tutorialspoint.com/python/python_overview.htm')
read = response.read()
print(read)
markup = BeautifulSoup(read, 'html.parser').prettify()
print(markup[:100])

print(markup.title)

for x in BeautifulSoup(read, 'html.parser').find_all('b'):
    print(x.string)

