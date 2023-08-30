# no_of_list = int(input("How many items add in a list: "))
n = int(input("Enter a list element separated by space: "))
# list = input_string.split()
t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
if t==1:
    ls = [i for i in range(n)]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f'item{i}': i for i in range(n)}
    print(dict1)
    print(type(dict1))
elif t==3:
    s ={i for i in range(n)}
    print(s)
    print(type(s))
else:
    print("you have enter the wrong input")