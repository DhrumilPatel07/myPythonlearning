f = open("dhrumil.txt")
f.seek(1)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
