import datetime
today=datetime.date.today()
print(today)
print()

time=datetime.time(20,10,00)
print(time)
print()

now=datetime.datetime.now()
print(now)
print()

year=today.year
print(year)
month=today.month
print(month)
day=today.day
print(day)
print()

weekday=today.weekday
print(weekday)
isoweekday=today.isoweekday
print(isoweekday)
replace=today.replace(year=2004)
print(replace)
print()

now=datetime.datetime.now() 
hour=now.hour 
minute=now.minute 
second=now.second  
print(hour,minute,second)
replace=now.replace(hour=2)
print(replace)
microsecond=now.microsecond 
print(microsecond) 
print() 

dt=datetime.datetime(2004,6,11,15,23,55)
print(dt.time) 
print(dt.date)
print(dt.month)
print(dt.year)
print(dt.second)
print(dt.day)
print(dt.hour)
print()  
formatted=dt.strftime("%Y-%m-%d %H-%M-%S")
print(formatted) 
parsed=datetime.datetime.strptime("2024-10-05 20-07-15","%Y-%m-%d %H-%M-%S")
print(parsed)
print()  
