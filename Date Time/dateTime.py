from datetime import *
now = datetime.now()
print(str(now))
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.strftime('%d-%m-%Y %H:%M:%S'))  # format given is case sensitive
print(now.isoformat())
