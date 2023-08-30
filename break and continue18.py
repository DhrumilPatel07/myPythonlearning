i = 0

"""while (True):
    if i+1<5:
        i = i + 1
        continue

    print(i+1, end=" ")
    if(i==44):
        i = i + 1
        break
    i = i + 1
"""

#Quiz

while(True):
    inp = int(input("Enter the number: \n"))
    if inp>=100:
        print("congrats you have enter the number greter than 100\n ")
        break
    else:
        print("try again!\n")
        continue
