import datetime

# TIME object
# datetime.time(hour,minutes,secs) goes all the way to microsecond and more
# goes by 24h clock
mytime=datetime.time(2,20,57)

print(mytime.minute)
print(mytime)

# DATE object

today=datetime.date.today()

print(today)
print(today.month)
# C-time formatting
print(today.ctime())


# DATE and TIME object
from datetime import datetime

mydatetime=datetime(2021,10,3,14,21,1)

print(mydatetime)

# you can replace values by using replace - does not happen in place- needs new assignment
mydatetime=mydatetime.replace(year=2022)
print(mydatetime)


# datetime calculations
from datetime import date

date1=date(2021,11,3)
date2=date(2020,11,3)

print((date1-date2).days)
