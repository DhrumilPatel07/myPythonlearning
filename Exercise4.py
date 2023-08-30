try:
    print("How many star you want:")
    n = int(input())
    print("type 1 or 0")
    m = int(input())
    if m!=0 and m!=1:
        raise Exception('Please enter valid value')

    new = bool(m)
    if new == True:
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end = " - ")
            print()

    elif new == False:
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print("*", end="")
            print()

except Exception as e:
    x = e.args
    print(x)


exit(200)