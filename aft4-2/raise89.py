# a = input("What is your name ")
# b = input("how much do you earn")
# if b==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("Number are not allowed")
#
# print(f"Hello {a}")

c = input("Enter your name")
try:
    print(a)

except Exception as e:
    if c == "dhrumil":
        raise ValueError("Dhrumil is blocked he is not allowed")

    print("Exception handled")