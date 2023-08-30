# f = open("dhrumil.txt", "w")
# a = f.write("Dhrumil is good boy")
# print(a)
# f.close()

# f = open("dhrumil2.txt", "a")
# a = f.write("Dhrumil is a good boy\n")
# print(a)
# f.close()

# handle read and write

f = open("dhrumil2.txt", "r+")
print(f.read())
f.write("thank you")
