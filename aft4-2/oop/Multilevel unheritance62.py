class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.guitar)



# ------------------------------EXERCISE--------------------------------


class elecdevice():
    no_of_phone = 4

class pocketgud(elecdevice):
    no_of_phone = 2

    def hasphone(self):
        return f"i am manager and i have {self.no_of_phone} phone"

class phone(pocketgud):
    pass
    # no_of_phone = 1

    # def hasphone(self):
    #     return f"hey there! i have {self.no_of_phone} phone"

amit = elecdevice()
vishal = pocketgud()
Dhrumil = phone()

print(Dhrumil.hasphone())