import time
import calendar
localtime = time.localtime(time.time())
print(time.time())
print('Local current time:', localtime)

localtime = time.asctime(time.localtime(time.time()))
print('Local current time:', localtime)
cal = calendar.month(2018, 7)
print(cal)
