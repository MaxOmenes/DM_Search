import sys


class BasicSearch:
    name = "Basic"
    minTime = sys.maxsize
    maxTime = -sys.maxsize
    allTimes = 0
    count = 0

    def __init__(self):
        pass

    def search(self, arr, a):
        pass

    def getName(self):
        return self.name

    def getMinTime(self):
        return self.minTime

    def getMaxTime(self):
        return self.maxTime

    def getAvgTime(self):
        return self.allTimes / self.count

    def setTime(self, a):
        if a < self.minTime:
            self.minTime = a
        elif a > self.maxTime:
            self.maxTime = a

        self.count += 1
        self.allTimes += a
