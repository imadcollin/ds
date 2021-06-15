#%%
import datetime

print('------Date Time Representation------')
print(datetime.datetime.today())
dateTime = datetime.date.today()
print('Year: ', dateTime.year)
print('Month: ', dateTime.month)
print('Day: ', dateTime.day)
print('Month Name : ', dateTime.strftime('%B'))
print('Week Name : ', dateTime.strftime('%A'))

print('------Date Time Arithmetic------')
day1 = datetime.date(2020, 11, 10)
print('Day1: ', day1.ctime())
day2 = datetime.date(2015, 3, 5)
print('Day2: ', day2.ctime())

print('Diff: ', day1 - day2)

deltaOfFourDays = datetime.timedelta(days=4)
print('Four days befor: ', datetime.date.today() - deltaOfFourDays)
print('Four days after: ', datetime.date.today() + deltaOfFourDays)

print('------Date Time Comparison------')
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
if today == tomorrow:
    print('today==tomoroow')
else:
    print('today !=tomorrow')
# %%
