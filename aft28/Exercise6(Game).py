import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
your_point = 0

print("\t\t\t\t\tWelcome to my game\n")
print("s for snake \nw for water\ng for gun")

while no_of_chance < chance:
    _input = input('Snake,water,gun\n')
    _random = random.choice(lst)

    if _input == _random:
        print("tie Both 0 point to each\n")

    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("computer wins 1 pont")
        print(f"computer point is {computer_point} and your pont is {your_point}")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("computer wins 1 pont")
        print(f"computer point is {computer_point} and your pont is {your_point}")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("computer wins 1 pont")
        print(f"computer point is {computer_point} and your pont is {your_point}")

    elif _input == "g" and _random == "s":
        your_point = your_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("you wins 1 pont")
        print(f"computer point is {computer_point} and your pont is {your_point}")

    elif _input == "w" and _random == "g":
        your_point = your_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("you wins 1 pont")
        print(f"computer point is {computer_point} and your pont is {your_point}")

    elif _input == "s" and _random == "w":
        your_point = your_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("you wins 1 pont")
        print(f"computer point is {computer_point} and your pont is {your_point}")

    else:
        print("your input is wrong! try again!!\n")

    no_of_chance = no_of_chance + 1
    print(f"{chance-no_of_chance} chance lef out of {no_of_chance}")


print(f"\nyour point is {your_point} and compute point is {computer_point}")
if computer_point == your_point:
    print("Tie")

elif computer_point > your_point:
    print("computer win this game")

else:
    print("you win this game")

print("\nGame over!!")

# pl = int(input("Would you like to play again!!\n1.yes\n2.No"))
# if pl == 1:
#     print("welcome back to the game\n")
#     continue
# elif pl == 2:
#     print("Thank you for playing this game")
#     break
# else:
#     print("pleas enter the valid option")



