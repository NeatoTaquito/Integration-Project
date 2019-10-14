#Daniel Claus Romeo
#Choose Your Own Adventure
#Last Edited: 10/14/19

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
        print("Welcome, Player. Before you lies a divide, which splits into two openings for two possible paths.")
        sleep(1)
        answer = input("Do you:\n(1)go left? \n(2)go right?")
# I add the option of 1 or 2 so that the input can have a bit more simplicity. I'm afraid of it breaking the loop more often then helping the user progress.
        if answer == "2":
            print("You choose right, right? Awesome! Ok, off we go. You pass normal everyday foliage; yet, strung along a bush you see an ornate necklace.")
            sleep(1)
            answer=input("Do you:\n(1)pick it up and put it in your bag\n(2)or do you leave it be?")
            if answer == "1":
                sleep(1)
                print("You pick it up and almost immediately it trembles, as if calling for you to try it on.")
                answer=input("Do you:\n(1)put it on?\n(2)or place it in your bag instead?")
                sleep(1)
                if answer == "1":
                    sleep(1)
                    print("You place it around your neck, you instantly transform into a fern; similar to the one you had just picked this up from.")
                    sleep(1)
                    answer=input("Sorry," + " " + name + ". Better luck next time. \n(1)Wanna try again?\n(2)Accept your fate?")
                    if answer == "2":
                       print("Thanks for playing," + name + "!") 
                    elif answer == "1":
                        break

# I've begun to add more print statements to my lines of code leading up to the input to not only increase the novelization of the story, but to also ensure that we keep the lines relatively small.                    
                if answer == "2":
                    print("You chose to put it in your bag. After getting back on the trail something like a whisper calls out to you.")
                    sleep(1)
                    print(name,", I need your help. If you go past the fern you'll find a cottage; in there I am being held captive!")
                    sleep(1)
                    answer = input("Do you:\n(1)listen to this ominous voice?\n(2)ignore it an continue on the path?")
                    if answer == "1":
                        print("You decide to listen to this voice and use their directions to head to the cottage(since you've nothing better to do).")
                        sleep(1)
                        print("Just like the voice said, the incredibly vacant seeming cottage lay rotten and sunken before you.")
                        sleep(1)
                        print("The voice then beckons you to enter using the basement doors on the left;yet, there seems to be a perfectly good front door.")
                        sleep(1)
                        answer = input("Do you:\n(1)listen to the voice?\n(2)Or use the front door?")
                        if answer == "1":
                            print("You figure if you've already listened thus far, you might as well continue to do so.")
                            sleep(1)
                            print("As you make your way to the basement doors, the air starts to shift and carry a strange weight to it.")
                            sleep(1)
                            print("You feel your bag tremble with anticipation as the voice you hear rings out again.")
                            sleep(.5)
                            print(name + ", don't back down now. I'm counting on you.")
                            sleep(1)
                            print("You hands, clammy and cold, reach for the door but before your hands meet with the knob the doors swing open.")
                            sleep(1)
                            answer=input("Do you:\n(1)go inside?\n(2)or turn back to use the door?")
                            if answer == "1":
                                print("You bravely step forward, into the dimly light basement.")
                                sleep(1)
                                print("Almost like in a horror film, the doors slam shut behind you as you reach the foot of the stairs.")
                                sleep(1)
                                print("Before you stands a statue of a kneeling woman, covered in vines with its hands reaching out in a cupped form.")
                                sleep(1)
                                print("The Voice calls out to you again.\n'There I am. I need you to place the necklace into my frozen hands. It will bring me back so that I may aid you.")
                                sleep(1)
                                print("Almost as soon as the Voice stops, a tattered figure you failed to see brings itself into the light.")
                                print("It's a woman drenched in sweat and mud, her hands chained to the wall. As she slunched forward you hear her cry out to you.")
                                sleep(1)
                                print("'Please..that necklace....that's mine.' she croaks.\n Her voice sounded just like the one in your head.")
                                answer = input("Do you:(1)listen to the Voice in your head and place the necklace into the hands of the statue?\n(2)or place it around the neck of this somehow familiar woman?")
                                if answer == "1":
                                    print()
                                elif answer == "2":
                                    print()

                            elif answer == "2":
                                print("Almost as quickly as the doors swing open, you book it to the front door; crashing into it and nearly sending the door off the hinges.")
                                sleep(1)
                                print("Three hooded figures with foliage wrapped around themselves stand before you. The middle one raises its hand out to your bag.")
                                print("You medallion tremors with the force of an earthquake and rips through your bag, into the hand of the hooded figure.")
                                sleep(1)
                                print("The figure, now grasping the medallion, starts to make a rustling sound similar to falling leaves from rushing wind.")
                                print("The sound grows increasingly louder as each moment passes, and your vision starts to fade almost as quickly.")
                                sleep(1)
                                print("You've been turned into a statue, in the bottom of some unknown place. The only thing you can do is think.")
                                print("Sorry," + name + " seems you've met a standstill. Better luck next time.")
                                break
    
                            
            elif answer == "2":
                print("You ignore the necklace and continue your walk.\nAs you walk the air becomes more arid and hotter in temperature.")
                sleep(1)

        elif answer=="1":
            input()
chooseYourOwnAdventure()
