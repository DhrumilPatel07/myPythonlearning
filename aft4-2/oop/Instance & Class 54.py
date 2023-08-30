class Employes:
    no_of_leave = 4
    pass

Dhrumil = Employes()
Rohan = Employes()

Dhrumil.name = "Dhrumil"
Dhrumil.roll = 7
Dhrumil.mark = 99
# Dhrumil.no_of_leave = 2

Rohan.name = "Rohan"
Rohan.roll = 1
Rohan.mark = 79


print(Dhrumil.__dict__)
print(Employes.no_of_leave)
Employes.no_of_leave = 2

print(Rohan.__dict__)
print(Employes.no_of_leave)