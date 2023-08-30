print("enter the 1st number")
num1 = int(input())
print("choos the type for calculation from this", "+, -, /, *" )
num3 = input()
print("enter the 2nd number")
num2 = int(input())


if num1 == 45 and num2 == 3 and num3 == '*':
    print("154")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '+':
    num4 = num1+num2
    print(num4)
elif num3 == '-':
    num4 = num1 - num2
    print(num4)
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '/':
    num4 = num1 / num2
    print(num4)
"""else num3 == "**":
    num4 = num1 ** num2
    print("num4")"""