a = int(input('Enter a: '))
b = int(input('Enter b: '))
try:
    password = '007'
    x = a/b
    li = [1, 2, 3, 4]
    print('Output', x)
except ZeroDivisionError as ze:
    print('Exception is', ze)
finally:
    password = ''
    print('Pass', password)
    print('Hi finally')
print('I am still running')
