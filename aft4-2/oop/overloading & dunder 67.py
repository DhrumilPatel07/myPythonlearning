class student:
    pass

    def __init__(self, aname, aroll, amark):
        self.name = aname
        self.roll = aroll
        self.mark = amark

    def printdetails(self):
        return f"the name is {self.name}. his roll number is {self.roll}. his mark is {self.mark}"

    def __add__(self, other):
        return self.mark + other.mark

    def __truediv__(self, other):
        return self.mark / other.mark

    def __repr__(self):
        return f"{self.name} is good student. {self.mark}, {self.roll}"

# -----------------------------------QUIZ-----------------------------------------

    def __mul__(self, other):
        return self.mark * other.mark
    def __sub__(self, other):
        return self.mark - other.mark

dhrumil = student("Dhrumil", 7, 99)
rohan = student("Rohan", 1, 77)

print(dhrumil * rohan)
print(dhrumil - rohan)

print(dhrumil / rohan)
print(dhrumil.__repr__())





