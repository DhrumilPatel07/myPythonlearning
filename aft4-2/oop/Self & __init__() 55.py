# ---------------------------------- __INIT__() ------------------------------------------

class Employes:
    pass

    def __init__(self, aname, aroll, amark):
        self.name = aname
        self.roll = aroll
        self.mark = amark

Dhrumil = Employes("Dhrumil", 7, 99)
Rohan = Employes("Rohan", 1, 79)
print(Dhrumil.__dict__)
# print(Rohan.__dict__)


# -------------------------------------SELF---------------------------------------------

class Employes:
    no_of_leave = 4
    pass

    def printdetails(self):
        return f"\nThe name is {self.name}. His Roll number is {self.roll}. His mark is {self.mark}"

Dhrumil = Employes()
Rohan = Employes()

Dhrumil.name = "Dhrumil"
Dhrumil.roll = 7
Dhrumil.mark = 99

Rohan.name = "Rohan"
Rohan.roll = 1
Rohan.mark = 79

print(Rohan.printdetails())