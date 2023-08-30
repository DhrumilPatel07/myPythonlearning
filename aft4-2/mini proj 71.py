class Library:
    def __init__(self, List, name):
        self.booklist = List
        self.name = name
        self.lenddict = {}

    def DisplayBook(self):
        print(f"We have following book in our library : {Dhrumil.name}")
        for key, book  in enumerate(self.booklist):
            print(key, book)

    # def LandBook(self, user, book):
    #     if book not in self.lenddict.keys():
    #         self.lenddict.update({book: user})
    #         print(self.lenddict)
    #         print("Lender-Book database has been updated. You can take the book now")
    #     else:
    #         print(f"Book is already being taken by {self.lenddict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print(self.booklist)
        print("your book has been added to book list")

    def checkBook(self, book):
        print(book in self.booklist)

    def deleteBook(self, book):
        self.DisplayBook()
        self.booklist.remove(book)
        self.DisplayBook()

    def deleteBookByKey(self, number):
        self.booklist.pop(num)
        self.DisplayBook()


if __name__ == '__main__':
    Dhrumil = Library(['Mahabharat', 'Ramayan', 'Bhagvat Gita', 'Harry Potter', 'Lord of the rings', 'bk'], "Dhrumillibrary")

    while(True):
        print(f"Welcome the {Dhrumil.name} Laibrary. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Delete Book")
        print("5. Check a Book is available in lib")
        print("6. Delete book by number")
        user_choice = input()

        if user_choice not in ['1', '2', '3', '4', '5', '6']:
            print("please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Dhrumil.DisplayBook()

        elif user_choice == 2:
            book = input("Enter the name of book you want to land:")
            user = input("Enter your name :")
            Dhrumil.LandBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of book you want to add:")
            Dhrumil.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of book you want to delete:")
            Dhrumil.deleteBook(book)

        elif user_choice == 5:
            book = input("Enter the name of book you want to return:")
            Dhrumil.checkBook(book)

        elif user_choice == 6:
            Dhrumil.DisplayBook()
            num = int(input("Enter the number of book you want to delete:"))
            Dhrumil.deleteBookByKey(num)

        else:
            print("not a valide option")

        while (True) :
            print("press q to Quit and enter any key to Continue")
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            else:
                break