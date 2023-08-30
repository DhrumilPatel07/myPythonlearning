# l = 10
# def function1(n):
#     # l=5
#     m = 10
#     global l
#     l = l + 45
#     print(l)
#     print(n, "the value of l is", l)
#
# function1("We have")

x = 89
def functiom1():
    x = 20
    def function2():
        global x
        x = 88
    print("before calling func2()", x)
    function2()
    print("after calling func2()", x)

functiom1()
print(x)