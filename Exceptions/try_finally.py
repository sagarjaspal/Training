with open('abc.txt', 'a+') as f: #this method closes the file automatically
    f.write('Hello all')         #after completion of operation
print(f.closed)

f1 = open('ram.txt', 'a+')

try:
    f1.write('Hi')+402
    print(f1.closed)
finally:
    f1.close()
    print('File is now closed')
    print(f1.closed)
