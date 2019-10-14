#Daniel Claus Romeo
#Choose Your Own Adventure
#10-13-19: Last Edited.

# I am about to add a timer to polish up how quickly the text comes after getting user input.
from time import sleep
#I'm adding a definition to my function below so that I may be able to use "Recursion" to bring any deaths or game overs to the beginning of the while loop.
def chooseYourOwnAdventure():
    answer = True
    while answer == True:
        name = input("What is your name, stranger?")
        sleep(1)
        print("Greetings," + " " + name + ". Let's begin.")
        sleep(2)
        answer = input("Welcome, Player. Before you lies a divide, which splits into two openings for two possible paths. Do you:\n(1)go left? \n(2)go right?")
        sleep(1)
# I add the option of 1 or 2 so that the input can have a bit more simplicity. I'm afraid of it breaking the loop more often then helping the user progress.
        if answer == "2":
            answer = input("You choose right, right? Awesome! Ok, off we go. You pass normal everyday foliage; yet, strung along a bush you see an ornate necklace. Do you:\n(1)pick it up\n(2)or do you put it in your bag?")
            sleep(1)
            if answer == "1":
                answer = input("You pick it up and almost immediately it trembles, as if calling for you to try it on. Do you:\n(1)put it on?\n(2)or place it in your bag instead?")
                sleep(1)
                if answer == "1":
                    sleep(1)
                    input("You place it around your neck, you instantly transform into a fern; similar to the one you had just picked this up from. \nSorry," + " " + name + ". Better luck next time. \n(1)Wanna try again?\n(2)Accept your fate?")
                    if answer == "Yes":
                        answer = False
                if answer == "2":
                    print("You chose to put it in your bag. After getting back on the trail something like a whisper calls out to you." \n name,", I need your help. If you go past the fern you'll find a cottage; in there I am being held captive.\n Do you:\n(1)list to this ominous voice\n(2)ignore it an continue on the path?")
                    if answer == "1":
                        input("You decide to listen to this voice and use their directions to head to the cottage(since you've nothing better to do).


        elif answer=="1":
            input()
chooseYourOwnAdventure()
