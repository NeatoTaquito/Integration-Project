def diceRoll():
    input("Would you like to play a dice game? Maybe you'll have better luck!")
    if "yes":
        from random import randint
        repeat = True
        while repeat:
            print("You rolled",randint(1,6))
            print("Do you want to roll again?")
            repeat = ("y" or "yes") in input().lower().strip()
    else:
        print("Well, fine! I didn't want to play with you anyway!!!")
        break

diceRoll()