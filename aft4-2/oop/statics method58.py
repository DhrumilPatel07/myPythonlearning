class Employes:
#     no_of_leave = 4

    # def __init__(self, aname, aroll, amark):
    #     self.name = aname
    #     self.roll = aroll
    #     self.mark = amark

    # @classmethod
    # def change_leaves(cls, newleave):
    #     cls.no_of_leave = newleave

    # @classmethod
    # def from_dash(cls, text):
    #     # param = string.split("-")
    #     # print(param)
    #     # return cls(param[0],param[1],param[2])
    #     return cls(*text.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good " + string)

Employes.printgood("Dhrunil")

# Dhrumil = Employes("Dhrumil", 7, 99)
# Rohan = Employes("Rohan", 1, 79)
# karan = Employes.from_dash("Karan-2-66")
# Employes.no_of_leave = 5



# print(karan.no_of_leave)
# print(karan.__dict__)
# Rohan.change_leaves(45)
# print(Dhrumil.no_of_leave)