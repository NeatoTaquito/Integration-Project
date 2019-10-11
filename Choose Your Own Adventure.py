#Daniel Claus Romeo
#Choose Your Own Adventure
#10-9-19: Last Edited.
while True:
    #".lower().strip()" is used to accept any input by the user and strip any spaces they may add and make their input into all lower case.
    answer = input("Welcome, Player. Before you lies a divide, which splits into two openings for two possible paths. Do you go left, or right?(1 or 2)").lower().strip()
    # I add the option of 1 or 2 so that the input can have a bit more simplicity. I'm afraid of it breaking the loop more often then helping the user progress.
    if answer == "2" or answer == "right":

            answer = input("You choose right, right? Awesome! Ok, off we go. You pass normal everyday foliage; yet, strung along a bush you see an ornate necklace. Do you pick it up(1), or do you put it in your bag(2)").lower().strip()
            if answer == "pick it up" or answer == "1":

                answer = input("You pick it up and almost immediately it trembles, as if calling for you to try it on. Do you put it on (1) or place it in your bag instead (2)?").lower().strip()
                if answer == "put it on" or "1":
                    answer == ("As you place it around your neck, you instantly transform into a pig.")
                    break

                if answer == "2" or answer == "place it in your bag" or answer =="place it in my bag":

    elif answer == "left" or answer == "1":
        input()