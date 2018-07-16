from threading import *
from time import *


class Clock(Thread):
    def __init__(self, h, m, s):
        Thread.__init__(self)
        self.h = h
        self.m = m
        self.s = s

    def run(self):
        for hh in range(self.h, 13):
            for mm in range(self.m, 61):
                for ss in range(self.s, 61):
                    ntime = str(hh)+':'+str(mm)+':'+str(ss)
                    print(ntime)
                    sleep(1)
                self.s = 1
            self.m = 1
        self.h = 1


c = Clock(4, 12, 0)
c.start()
