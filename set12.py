s = set()
#print(type(s))
#l = [1, 2, 3, 4]
#s_from_list = set(l)
#print(s_from_list)
#print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(1)
s1 = {4, 5}
print(s.isdisjoint(s1))
print(s)