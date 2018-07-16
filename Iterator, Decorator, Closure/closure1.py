def nInto(n):
    def multiplier(m):
        return n*m
    return multiplier


a = nInto(5)
print(a(20))
