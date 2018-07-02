from MyExcept import *
i = 20
try:
    if i < 30:
        raise MyExcept('No. must be greater than 30')
except MyExcept as me:
    print(me)
