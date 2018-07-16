def printme(msg):
    def print():
        return msg
    return print


a = printme('Function Closure')
print(a())

