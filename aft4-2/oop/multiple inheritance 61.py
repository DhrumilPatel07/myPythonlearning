class student:
    no_of_leave = 4

    def __init__(self, aname, aroll, amark):
        self.name = aname
        self.roll = aroll
        self.mark = amark

    def printdetails(self):
        return f"The first student is {self.name}. His roll number is {self.roll}. His mark is {self.mark}"

    # @classmethod
    # def change_leaves(cls, newleave):
    #     cls.no_of_leave = newleave

    @classmethod
    def from_dash(cls, text):
        # param = string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return cls(*text.split("-"))

class player:
    no_of_game = 5
    def __init__(self,aname ,agame):
        self.name = aname
        self.game = agame

    def printdetails(self):
        return f"The second Student is {self.name}. he would like to play {self.game}"

class coolprogramr(student, player):
    pass

# Dhrumil = student("Dhrumil", 7, 99)
# Rohan = student("Rohan", 1, 79)

karan = player("Karan", ["cricket"])
shubham = coolprogramr("Shumbham", 10, 88)

# det = shubham.printdetails()
print(shubham.printdetails())

print("\nlet's talk about karan:")
print(karan.printdetails())
print(karan.__dict__)
print("he played", karan.no_of_game, "game")