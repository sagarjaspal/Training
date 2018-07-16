def make_pretty(func):
    def inner():
        print('Inner function')
        func()
    return inner


# def ordinary():
#    print('I am ordinary')


# a = make_pretty(ordinary)
# print(a())


@make_pretty
def ordinary():
    print('I am decorated ordinary')


b = ordinary()
print(b)
