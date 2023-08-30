n = 5
no_of_guess = 1
while(True):
    inp = int(input("guess the number :"))
    print(9-no_of_guess,"no. of guess left")
    no_of_guess = no_of_guess + 1
    if no_of_guess > 9:
        print("game over!")
        break
    if inp == 27:
        print("congratulation! you guess the correct number")
        break

    elif inp <= 30 and inp > 27 :
        print("you are near! the number is little smaller")
        continue

    elif inp >= 24 and inp < 27 :
        print("you are near! the number is little bigger")
        continue

    elif inp < 24 :
        print("the number is bigger than this")
        continue

    else:
        print("the number is smaller than this")
        continue




