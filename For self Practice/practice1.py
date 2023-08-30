def fibonacci(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input("enter number:"))

for n in range(number):
    print(fibonacci(n+1))

print("your fibonacci number is", fibonacci(number))



