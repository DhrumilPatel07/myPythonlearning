class Employes:
    no_of_leave = 4

    def __init__(self, name, lang, id):
        self.name = name
        self.lang = lang
        self.id = id

    # @classmethod
    # def change_leaves(cls, newleave):
    #     cls.no_of_leave = newleave

    @classmethod
    def from_dash(cls, text):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return cls(*text.split("-"))

    def getEmployeeName(self):
        return self.name

    def getEmployeeId(self):
        return self.id

class programer(Employes):

    def __init__(self, name, lang, id):
        self.name = name
        self.lang = lang
        self.id = id

    def printprog(self):
        return f"the programmer's name {self.name}. his roll num is {self.roll}. his mark is {self.mark} "

    def getlang(self):
        return self.lang

employesObj = Employes("Dhrumil", 7, 99)
print(employesObj.getEmployeeName())
print(employesObj.getEmployeeId())
print(employesObj.getlang())
#Rohan = Employes("Rohan", 1, 79)


prObj = programer("Karan", "Python", "KTPL631")
#vishal = programer("Vishal", 3, 88)
print(prObj.getEmployeeId())
print(prObj.getlang())
print(prObj.getEmployeeName())


