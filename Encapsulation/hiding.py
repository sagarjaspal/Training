class MethodHiding:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 30

    def __show(self):
        print('Hello')
    def _display(self):
        print('Hi')


ob = MethodHiding()
ob._display()
print(ob.x)
print(ob._y)
print(ob.__z)
ob.__show()
