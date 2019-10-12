#Daniel Claus Romeo
#Choose Your Own Adventure
#10-11-19: Last Edited.

answer = True
name = input("What is your name, stranger?")
print("Greetings," + " "name + ". Let's begin.")
while True:
    name = input("What is your name, stranger?")
    print ("Greetings," + " " name + ". Let's begin.")
    print(input("Welcome, Player. Before you lies a divide, which splits into two openings for two possible paths. Do you go left, or right?(1 or 2)"))
    # I add the option of 1 or 2 so that the input can have a bit more simplicity. I'm afraid of it breaking the loop more often then helping the user progress.
    if answer == "2":
        answer = input("You choose right, right? Awesome! Ok, off we go. You pass normal everyday foliage; yet, strung along a bush you see an ornate necklace. Do you pick it up(1), or do you put it in your bag(2)")
            if answer == "1":

                answer = input("You pick it up and almost immediately it trembles, as if calling for you to try it on. Do you put it on (1) or place it in your bag instead (2)?")
                if answer == "put it on" or "1":
                    answer = ("As you place it around your neck, you instantly transform into a pig. \nSorry, " + name)

                if answer == "2":

    elif answer =="1":
        input()