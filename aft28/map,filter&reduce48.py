#------------------------------MAP-----------------------------------

# number = ["12", "24", "45"]
# number = list(map(int, number))

# for i in range(len(number)):
#     number[i] = int(number[i])

# number[2] = number[2] + 1
# print(number[2])


# def sq(a):
#     return a*a

# num = [2,5,4,8,6,1,5,55,4,7]
# square = list(map(sq, num))
# print(square)

# num = [2,5,4,8,6,1,5,55,4,8]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square, cube]
# num = [2,5,4,8,6,1,5,55,4,8]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)


# ------------------------------FILTER-----------------------------------

# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def is_grater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_grater_5, list_1))
# print(gr_than_5)


# -----------------------------REDUCE--------------------------------------

from functools import reduce

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)