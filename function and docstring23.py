# a = 9
# b = 8
# c = sum((a,b)) # built in function
# print(c)

def function1(a,b):
    print("hello you are is function 1", a+b)

def function2(a,b):
    """this is a function which is the calculate the number of two
    this doesn't work for three numbers"""
    average = (a+b)/2
    print(average)
    return average

#v = function2(5, 7)
#print(v)
print(function2.__doc__)


