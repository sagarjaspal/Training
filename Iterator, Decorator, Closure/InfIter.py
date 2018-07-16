# make infinite iterator


class InfIter:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


a = InfIter()
i = iter(a)
next(i)
