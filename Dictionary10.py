# Dictionary is nothing but key value pairs

d1 = {}
#print(type(d1))
d2 = {"harry" : "burger",
      "abhinav" : "roti",
      "virat" : "dal",
      "aman" :{"b" :"bhaji", "a" : "bhindi", "c" : "pizza"}}

#d2["ankit"] = "jumk food"
#d2[420] = "kabab"
#print(d2)
#del d2[420]
#print(d2)
#print(d2["aman"])

#d3 = d2.copy()
#del d3["harry"]
#print(d3)

d2.update({"leena" : "toffee"})
print(d2.keys())
#print(d2.items())