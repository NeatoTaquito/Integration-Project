#Daniel Claus Romeo
#Mood Guesser
#https://www.youtube.com/watch?v=DEcFCn2ubSg&t=438s is referenced URL for the use of the ".lower().strip()" for the imput to not negatively afflict the user

value1 = 2
value2 = 2


hello = input("Hello! Welcome to my mood guesser; would you like to start? (yes/no)").lower().strip()
if hello == "no":
    print("Well, then. I guess I don't need to ask how you're feelin afterall....Jerk.")
elif hello == "yes":
    response = input(" Awesome! If you are feeling happy enter 1, and if you are not, enter 2.").lower().strip()
    if response == "2":
        print(" I'm sorry to hear that; but things will get better. If you need me I'm sorry to say but the guy who wrote this code doesn't know how to do that quite yet.")
    if response == "1":
        print("Wahoo! You are a happy person! As I am merely code, I can only deduce that this leads to positive outcome. My creator has not coded in 'happiness' quite yet.")
else:
    print("Well?...What's it gonna be pal?!")
arithmetic = input("Now that I know that you are feeling, can you solve an equation? What is 2 + 2").lower().strip()

if arithmetic == "4":
    print( value1 + value2 + ":" + "You're right!! Look at you meeting minimum requirements")
else:
    print("Really? Hoo boy, I think you should try again.")
