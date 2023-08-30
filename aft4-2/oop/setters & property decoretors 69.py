class Employee:
    def __init__(self, fname, lname,):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set. please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Dhrumil = Employee("Dhumil", "Patel")
rohan = Employee("Rohan", "zala")

print(Dhrumil.email)

Dhrumil.fname = "Dp"

print(Dhrumil.email)
Dhrumil.email = "this.that@gmail.com"

print(Dhrumil.email)

del Dhrumil.email
print(Dhrumil.email)
Dhrumil.email = "Harry.parry@gmail.com"
print(Dhrumil.email)