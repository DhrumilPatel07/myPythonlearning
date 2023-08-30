"""var1 = 6
var2 = 56
var3 = int(input())

if var3 > var2:
    print("greater")

elif var3 == var2:
    print("equle")

else:
    print("lesser")"""

#Quiz

age = int(input("enter your age: "))

if age<7 or age>100:
    print("not a logical age")

elif age > 18:
    print("you can drive")
elif age < 18:
    print("you can not drive")

else:
    print("you have to give the test")