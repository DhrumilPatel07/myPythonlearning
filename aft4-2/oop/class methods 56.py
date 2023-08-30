class Employes:
    no_of_leave = 4

    def __init__(self, aname, aroll, amark):
        self.name = aname
        self.roll = aroll
        self.mark = amark

    @classmethod
    def change_leaves(cls, newleave):
        cls.no_of_leave = newleave


Dhrumil = Employes("Dhrumil", 7, 99)
Rohan = Employes("Rohan", 1, 79)

Rohan.change_leaves(45)
print(Dhrumil.no_of_leave)   # dhrumil value bhi change thay kem ke class attribute ne pan change kare chhe




