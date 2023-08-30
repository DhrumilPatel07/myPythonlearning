# from abc import ABC, abstractmethod
from abc import ABC , abstractmethod

class shape:
    @abstractmethod
    def printarea(self):
        return 0


class rect:
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = rect()
print(rect1.printarea())