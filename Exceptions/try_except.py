a = int(input('Enter a: '))
b = int(input('Enter b: '))
try:
    x = a/b
    print('Output', x)
except ZeroDivisionError as ze:
    print('Exception is', ze)
print('I am still running')
