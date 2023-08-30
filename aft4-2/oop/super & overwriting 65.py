class A():
    classvar1 = "i am in class variabel class a"

    def __init__(self):
        self.var1 = "i am inside class A's constructor"
        self.classvar1 = "intance var in class A "
        self.special = "special"

class B(A):
    classvar1 = "i am in class B"

    def __init__(self):

        self.var1 = "i am inside class B's constructor"
        self.classvar1 = "intance var in class B "
        super().__init__()
        print(super().classvar1)

a = A()
b = B()

print(b.special, b.var1, b.classvar1)