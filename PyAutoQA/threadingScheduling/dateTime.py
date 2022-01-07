import datetime
import time

print(datetime.datetime.now())
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))
print(time.time())

now.strftime('%Y/%m/%d')
now.strftime('%Y/%m/%d %H:%M:%S')