import MyException
try:
    x = 10/0
    print(x)
except MyException:
    print('Divide by zero error')
