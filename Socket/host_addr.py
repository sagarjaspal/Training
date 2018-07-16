from socket import *

s = gethostname()  # for system name
print(s)

name = input('Enter host name:')
sn = gethostbyname(name)
print(sn)
