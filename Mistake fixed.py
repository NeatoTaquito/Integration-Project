#Daniel Claus Romeo
#Mood Guesser


you = "You "
lose = "lose!"

hello = input("Hello! Welcome to my mood guesser; would you like to start? (yes/no)")
if hello != ("no" or "yes"):
    print("Well?...What's it gonna be pal?!")
if hello == "no":
    print("Well, then. I guess I don't need to ask how you're feelin afterall....Jerk.")
if hello == "yes":
    response = input(" Awesome! If you are feelin Happy enter 1, and if you are not, enter 2.")
    if response == "2":
        print(" I'm sorry to hear that; but things will get better. If you need me I'm sorry to say but the guy who wrote this code doesn't know how to do that quite yet.")
    if response == "1":
        print("Wahoo! You are a happy person! I am jealous as I am having to write code while you vent to me....")
arithmetic = input("Now that I know that you are feeling, can you solve an equation? What is 2 + 2").strip()
if arithmetic != "4":
    print( you + lose)
if arithmetic == ("4"):
    print( "You're right!! Look at you meeting minimum requirements")
