class Employes:
    no_of_leave = 4

    def __init__(self, aname, aroll, amark):
        self.name = aname
        self.roll = aroll
        self.mark = amark
        self.tempNsme = 'xxxx'

    # @classmethod
    # def change_leaves(cls, newleave):
    #     cls.no_of_leave = newleave

    @classmethod
    def from_dash(self, text):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return self(*text.split("-"))

    def nameSplit(self, text):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return text.split("-")

    def getEmployeeNumber(self):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return self.getEmployeeNumberWithName()

    def getEmployeeNumberWithName(self):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return self.name + "  " + str(self.roll)

employesObj = Employes("Dhrumil", 7, 99)
#print(employesObj.nameSplit("Ronak-patel"))
print(employesObj.getEmployeeNumber())


Rohan = Employes("Rohan", 1, 79)
karan = Employes.from_dash("Karan-2-66")
# Employes.no_of_leave = 5

print(karan.no_of_leave)
print(karan.__dict__)
# Rohan.change_leaves(45)
# print(Dhrumil.no_of_leave)