#Daniel Claus Romeo
#Choose Your Own Adventure
#Last Edited: 11/18/19


# I am about to add a timer to polish up how quickly the text comes after getting user input.
from time import sleep
answer = True
# another while loop to break out when a wrong input is added or the game ends in a good or bad way.
while answer == True:
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
                    print("You place it around your neck, you instantly transform into a fern; similar to the one you had just picked the necklace up from.")
                    sleep(1)
                    print("Seems your curiousity has led you done a green state you werent quite expecting!")
                    print("Sorry," + " " + name + ". Better luck next time.")
                    sleep(3)
                    answer = False
                    sleep(2)

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
                                sleep(2)
                                print("'Please..that necklace....place it on my neck..save me!' she croaks.\n Her voice sounding more strained with each breath.")
                                print("'That statue, it lured me here too..cursed my to start turning into some bush..' Showing her leg, starting to break off into vines.")
                                print("After struggling to push herself back into the light, she croaks once more, 'Don't trust the Voice, help me....")
                                sleep(3)
                                print("Not knowing what to make of the situation, you have become tasked with an almost decision with two lives hanging on the outcome.")
                                print("What do you do?")
                                sleep(2)
                                answer = input("Do you:(1)listen to the Voice in your head and place the necklace into the hands of the statue?\n(2)or place it around the neck of this somehow familiar woman?")
                                if answer == "1":
                                    print("You trust the Voice as you have been and place the necklace into the statues cupped hands.")
                                    sleep(1)
                                    print("'No!...Dont-', before the lady could finish, the sound of howling wind and rushing leaves screams around the statue.")
                                    print("The statue then violently cracks off chunks of its stone prison fall from itself like hail.")
                                    sleep(2)
                                    print("The sound grew to a deafening level as the figure underneath the statue laid itself bare. Branches and vines shoot from the openings.")
                                    print("Some strike your arms and leg, almost instantly turning them to stone.'Fool', the wind seems to howl out; your vision fading with each strike.")
                                    sleep(2)
                                    print("You eventually succumb, unable to see nor feel. Only branching out with thoughts(no pun intended) as you become afixed in a dynamic pose.")
                                    sleep(3)
                                    print("Man, what a way to go. But hey, maybe you can call out to someone to help you out. Maybe they are just...walking about?")
                                    print("Better luck next time," + name + "!")
                                    sleep(2)
                                    answer = False
                                    sleep(2)
                                elif answer == "2":
                                    print("The Voice bellows while you place the necklace onto the neck of this stranger.")
                                    sleep(1)
                                    print("'NO! DO NOT BELIEVE HER SHE-'the Voice abruptly ends as it begins to almost splinter piece by piece from your decision.")
                                    print("With each broken piece from the statue, the woman seemed to grow in health and stature.")
                                    sleep(1)
                                    print("Evenutally all that remains of the Voice is silence and rubble; the woman now able to stand on her own. She asks:")
                                    sleep(1)
                                    print("'You have made the right choice, these evil beings tried to take everything from me; including my voice.'")
                                    sleep(1)
                                    answer = input("'Please, release me so I may stop these things before more are taken.\nDo you:\n(1)free her of her bonds?\n(2)Or leave her chained?")
                                    sleep(2)
                                    if answer == "1":
                                        print("You free her, the chains scattering to the ground as this overcoming sense of relief fills your mind.")
                                        sleep(1)
                                        print("She places a hand on your shoulder and places what seems to be a dagger into your bag.")
                                        print("'Thank you," + name + ". You've saved more than you can imagine.'")
                                        sleep(2)
                                        print("'Use that dagger to protect yourself if you need to; i'll rid this world of those Things.'")
                                        print("With that, she stormed out the basement and into the house; bright light shone through the floor boards unto you.")
                                        print("Eventually she comes back and gives the all clear, waving farewell as she disappears from view")
                                        sleep(3)
                                        print("Well, if that wasn't the weirdest thing to happen to you all day, but you succeeded!")
                                        print("Congratulations! You've completed obtained the first ending!")
                                        sleep(2)
                                        print("I implore you to try again and see what other adventures await! Or maybe, even play a dice game?")
                                        print("Either way, you did it!")
                                        sleep(2)
                                        answer = False
                                    elif answer == "2":
                                        print("'What? You must hurry, those Things heard their idol fall, they will be here any moment! Untie me!' As she screamed for help, the ceiling begins to crumble.")
                                        sleep(1)
                                        print("From three holes that were formed by the quakes seemed to drop three hooded figures; landing with weight comparable to beasts.")
                                        print("Out of the three, their middle hood rose the tallest and outstretched its 'hand'. It appearing to be a finger made of vines and fibers.")
                                        sleep(2)
                                        print("It pointed to the woman, her necklace, and the sound of howling wind and falling flora began to fill the air. The woman cried out;")
                                        print("'It's them! You idiot, they after this necklace! You've doomed us all!'Her face was pained, the necklace seeming to string outwards.")
                                        sleep(2)
                                        print("The necklace was struggling to go to the grasp of the middle figure, the howling growing louder by the second.")
                                        print("The medallion snaps off from the necklace and flies into the hands of the hooded Thing; the woman falling back down, immobile.")
                                        sleep(2)
                                        print("By now you see your limbs grow heavy and vision blurry. The figure now pointing to you; you turn to stone.")
                                        sleep(1)
                                        print("You chose an intersting end, didn't think you would come all this way just to turn around. Oh well!")
                                        print("Maybe next time you can find another way!")
                                        sleep(1)
                                        answer = False

                            elif answer == "2":
                                print("Almost as quickly as the doors swing open, you book it to the front door; crashing into it and nearly sending the door off the hinges.")
                                sleep(1)
                                print("Three hooded figures with foliage wrapped around themselves stand before you. The middle one raises its hand out to your bag.")
                                print("You medallion tremors with the force of an earthquake and rips through your bag, into the hand of the hooded figure.")
                                sleep(2)
                                print("The figure, now grasping the necklace, starts to make a rustling sound similar to falling leaves from rushing wind.")
                                print("The sound grows increasingly louder as each moment passes, and your vision starts to fade almost as quickly.")
                                sleep(2)
                                print("You've been turned into a statue, in the bottom of some unknown place. The only thing you can do is think to yourself.")
                                print("Sorry," + name + " seems you've met a standstill. Better luck next time.")
                                sleep(3)
                                answer = False
                                sleep(3)
    
                            
            elif answer == "2":
                print("You ignore the necklace and continue your walk.\nAs you walk the air becomes more arid and hotter in temperature.")
                sleep(1)
                print("It keeps climbing in temperature until you gain the sense to turn around.")
                print("But when you do, the trail you've known is just sand, same as what is around you as well.")
                sleep(2)
                print("Seems you've run into the old ' Walk until sand ' gag; but without a good punch line.")
                print("You eventually succumb to your thirst.")
                sleep(2)
                print("Yikes! That was actually pretty weird. I wonder why the developer even made this an option if you were doomed to start.")
                sleep(1)
                print(name + ", you are one tenacious tenant of this game. I emplore you to try again!")
                sleep(1)
                answer = False
                sleep(2)
#As I was focusing on the right-side path for the first half of this project, I plan on adding an additional and new story for heading left side. It will indeed be finished by the end of the project(10/20/19)
#I have now finished the left portion of the choose your own adventure novel/game (11/17/19) so now the final portion of the project can commence.
#This portion will have FAR MORE things happening; including even more stories.
        elif answer=="1":
            print("... you have just begun to feel you're walking into eternity when you see a T-junction. But just then you hear a ROAR!!!")
            sleep(1)
            input("You turn back to see a giant lion, miles away, running after you at great speed. You just have time to react. \nDo you:\n(1)dodge left?\n(2)or dodge right?")
            sleep(2)
            if answer == "1":
                print("Unfortunately for you, the lion catches up and rips you to shreds. You feel intense pain, yet you can't die. This is hell.")
                sleep(1)
                print("Better luck next time,"+ name + "!")
                answer = False
            elif answer == "2":
                 input("You find a portal to another dimension. Could this be a trap? Or should you take that chance?\nDo you:\n(1)Take said chance.\n(2)or do you continue on?")
                 sleep(1)
                 if answer == "1":
                     print("You have been walking for miles... and this is geting frustrating. Will this road ever end?")
                     sleep(1)
                     input("A dagger falls from the skies above.\nDo you:\n(1)allow it to strike you?\n(2)or do you dodge?")
                     if answer == "1":
                         print("You open your arms comically and allow this blade to make its impact; strangely it only embeds itself into your knee.")
                         sleep(2)
                         print("The searing pain that this knee sent throughout your body also strangely brings about a thought that you are done with adventuring.")
                         print("It seems to have also been laced with a toxin; as your eyes fog and your vision fades.")
                         sleep(2)
                         print("Seems like you are done," + name +". Man, you know I used to be an adventurer just like you.")
                         answer = False
                    elif answer == "2":
                        print("Leaping left, you dodge the strange looking knife. A few more come your way, allowing yourself even more dodges.")
                        sleep(1)
                        print("As the last knife sticks into the ground, you catch a glimpse of the assassin. It's...Cthulu?!")
                        sleep(1)
                        print("The tentacled assassin meets before you in all his Lovecraftian glory.")
                        sleep(1)
                        print("He speaks in 'blrrbss' and hisses, holding out his armed tentacle as if preparing for your retaliation.")
                        sleep(1)
                        print("What do you do? Do you:\n (1) grab a nearby knife and lunge at the God?\n(2) or do you become the next sacrfice for this deity?")
                        if answer == "1":
                            print("You go forth, knife in hand, thrusting it into the beard-like cluster of worm-like appendiges.")
                            sleep(1)
                            print("With a gurgle and a spit of ink, your knife finds its new home within the breast of this beast.")
                            sleep(1)
                            print("A geyser of ink hits your face, sending you in a fit trying to clear your vision.")
                            sleep(1)
                            print("Once you scrape away the effleuence of this fearsome foe, you find yourself back at the beginning of the crossroads again.")
                            sleep(2)
                            answer = False
                        elif answer == "2":
                            
        else:
            print("You need to choose either (1) or (2). Please try again!")
print("Thanks for playing!")
sleep(1)
#adding recursion so that I may have another way to add to this program after it is done with my first game I may have another to go with for the hell of it.
#The python interpreter is broken on my Pycharm for now so I am adding my additional file underneath the rest so it can be played through IDLE.
#I've also plans to make the generic dice roll game more fun with random snippits if it is a certain number, for fun.
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

