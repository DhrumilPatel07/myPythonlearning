def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow i would like to introduce some of our heros")

    for key, value in kwargs.items():
        print(f"{key} is a {value}")



normal = "These are the name"
har = ["Dhrumil", "krish", "amit", "Vishal", "Pranav"]
kw = {"Dhrumil" : "king", "Krish" : "Commander", "amit" :"Warrior", "Vishal" : "minister"}
funargs(normal, *har, **kw)