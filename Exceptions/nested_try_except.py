a = int(input('Enter a'))
b = int(input('Enter b'))
try:
    x = a/b
    li = [1, 2, 3, 4]
    print('Output:', x)
    print(li[8])
except ZeroDivisionError as ze:
    print(ze)
except IndexError as ie:
    print(ie)
print('Still in running mode')
