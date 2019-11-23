# Daniel Claus Romeo
# Choose Your Own Adventure
# Last Edited: 11/22/19

# I am about to add a timer to polish up how quickly the text comes after
# getting user input.
# I'm adding a definition to my function below so that I may be able to use
# "Recursion" to bring any deaths or game overs
# to the beginning of the while loop.
from time import sleep

name = input("What is your name, stranger?")
sleep(2)
print("Greetings, " + name + ". Let's begin.")
sleep(2)


def intro():
    """This is the heart of sole of the entire game; allowing the
    game to function. I did not put this story split into
    multiple functions as it would cause for a multitude of
    reformatting.
    For the future, I know this as an option now.

     __author__: Daniel Claus Romeo, 'w3schools.com' for the import
     sleep,
    POGIL's
    from class for if, while, and nested loops.

    """

    print("Welcome, Player. Before you lies a divide, which splits "
          "into two openings for two possible paths.")
    sleep(1)
    answer = input("Do you:\n(1)go left? \n(2)go right?")
    if answer == "2":
        right()
    elif answer == "1":
        left()
    else:
        variableError()


def right():
    """This segment choice took the longest to make, and I remember
    writing it all with a small little narrative in mind. I enjoyed
    writing this one.
    __author__ = Daniel Claus Romeo
    """
    print("You choose right, right? Awesome! Ok, off we go. You pass "
          "normal everyday foliage: yet, strung along a bush you see "
          "an ornate necklace.")
    sleep(1)
    answer = input("Do you:\n(1)pick it up and put it in your "
                   "bag\n(2)or do you leave it be?")
    if answer == "1":
        bag()
    elif answer == "2":
        leave()
    else:
        variableError()


def bag():
    print("You chose to put it in your bag. After getting back on "
          "the trail something like a whisper calls out to you.")
    sleep(1)
    print(name + ", I need your help. If you go past the fern "
                 "you'll find a cottage; in there I am being held "
                 "captive!")
    sleep(1)
    answer = input("Do you:\n(1)listen to this ominous voice?\n("
                   "2)ignore it an continue on the path?")
    if answer == "1":
        listen()
    elif answer == "2":
        path()
    else:
        variableError()


def listen():
    print("You decide to listen to this voice and use their "
          "directions to head to the cottage(since you've nothing "
          "better to do).")
    sleep(1)
    print("Just like the voice said, the incredibly vacant seeming "
          "cottage lay rotten and sunken before you.")
    sleep(1)
    print("The voice then beckons you to enter using the basement"
          "doors on the left;yet, there seems to be a perfectly good "
          "front door.")
    sleep(1)
    answer = input("Do you:\n(1)listen to the voice?\n(2)Or use the "
                   "front door?")
    if answer == "1":
        voice()
    elif answer == "2":
        frontDoor()
    else:
        variableError()


def voice():
    """This one is more of the narrative that is going to be more of a
    novel, but with the obvious end choice.
    __author__ = Daniel Claus Romeo
    """
    print("You bravely step forward, into the dimly light basement.")
    sleep(1)
    print("Almost like in a horror film, the doors slam shut behind "
          "you as you reach the foot of the stairs.")
    sleep(1)
    print("Before you stands a statue of a kneeling woman, covered in "
          "vines with its hands reaching out in a cupped form.")
    sleep(2)
    print("The Voice calls out to you again.\n'There I am. I need "
          "you to place the necklace into my frozen hands. It will "
          "bring me back so that I may aid you.")
    sleep(2)
    print("Almost as soon as the Voice stops, a tattered figure you "
          "failed to see brings itself into the light.")
    sleep(2)
    print("It's a woman drenched in sweat and mud, her hands chained "
          "to the wall. As she drags herself forward, you hear her "
          "cry out to you.")
    sleep(2)
    print("'Please..that necklace....place it on my neck..save me!' "
          "she croaks. \n Her voice sounding more strained with "
          "each breath.")
    sleep(2)
    print("'That statue, it lured me here too..cursed my to start "
          "turning into some bush..' Showing her leg, starting "
          "to break off into vines.")
    sleep(2)
    print("After struggling to push herself back into the light, "
          "she croaks once more, 'Don't trust the Voice, help me....")
    sleep(3)
    print("Not knowing what to make of the situation, you have "
          "become tasked with an almost decision with two lives "
          "hanging on the outcome.")
    sleep(2)
    answer = input("Do you:(1)listen to the Voice in your head and "
                   "place the necklace into the hands of the statue?"
                   "\n(2)or place it around the neck of this "
                   "somehow familiar woman?")
    if answer == "1":
        statue()
    elif answer == "2":
        woman()
    else:
        variableError()


def statue():
    """This ending was more so a deceit I was hoping to play to make
    the user think that they're going to make the right choice.
    __author__ = Daniel Claus Romeo
    """
    print("You trust the Voice as you have been and place the "
          "necklace into the statues cupped hands.")
    sleep(1)
    print("'No!...Don't-', before the lady could finish, the "
          "sound of howling wind and rushing leaves screams "
          "around the statue.")
    print("The statue then violently cracks off chunks of its "
          "stone prison fall from itself like hail.")
    sleep(2)
    print("The sound grew to a deafening level as the figure "
          "underneath the statue laid itself bare. Branches and "
          "vines shoot from the openings.")
    print("Some strike your arms and leg, almost instantly "
          "turning them to stone.'Fool', the wind seems to howl "
          "out; your vision fading with each strike.")
    sleep(2)
    print("You eventually succumb, unable to see nor feel. Only "
          "branching out with thoughts(no pun intended) as you "
          "become fixed in a dynamic pose.")
    dead()


def woman():
    """I brought this other choice to try and see if the user would
    still NOT trust the woman. Only the truly good may trust her
    blindly (like myself)
    __author__ = Daniel Claus Romeo
    """
    print("The Voice bellows while you place the necklace onto the "
          "neck of this stranger.")
    sleep(1)
    print("'NO! DO NOT BELIEVE HER SHE-'the Voice abruptly ends as "
          "it begins to almost splinter piece by piece from your "
          "decision.")
    print("With each broken piece from the statue, the woman seemed "
          "to grow in health and stature.")
    sleep(1)
    print("Eventually all that remains of the Voice is silence and "
          "rubble; the woman now able to stand on her own. She asks:")
    sleep(1)
    print("'You have made the right choice, these evil beings tried "
          "to take everything from me; including my voice.'")
    sleep(1)
    answer = input("'Please, release me so I may stop these things "
                   "before more are taken.\nDo you:\n(1)free her of "
                   "her bonds?\n(2)Or leave her chained?")
    if answer == "1":
        endingOne()
    elif answer == "2":
        leaveHer()
    else:
        variableError()


def endingOne():
    """"This was the first time I was able to think that the user
    deserved to win, so I wanted it to be pretty good! This was the
    weirdest ending though.
    __author__ = Daniel Claus Romeo
    """
    print("You free her, the chains scattering to the ground as this "
          "overcoming sense of relief fills your mind.")
    sleep(1)
    print("She places a hand on your shoulder and places what seems "
          "to be a dagger into your bag.")
    print("'Thank you," + name + ". You've saved more than "
                                 "you can imagine.'")
    sleep(2)
    print("'Use that dagger to protect yourself if you need to; "
          "I'll rid this world of those Things.'")
    sleep(1)
    print("With that, she stormed out the basement and into the "
          "house; bright light shone through the floor "
          "boards unto you.")
    print("Eventually she comes back and gives the all clear, "
          "waving farewell as she disappears from view")
    sleep(3)
    print(
        "Well, if that wasn't the weirdest thing to happen to you "
        "all day, but you succeeded!")
    win()


def leaveHer():
    print("'What? You must hurry, those Things heard their idol fall, "
          "they will be here any moment! Untie me!' As she "
          "screamed for help, the ceiling begins to crumble.")
    sleep(1)
    print("From three holes that were formed by the quakes seemed "
          "to drop three hooded figures; landing with weight "
          "comparable to beasts.")
    print("Out of the three, their middle hood rose the tallest "
          "and outstretched its 'hand'. It appearing to be a finger "
          "made of vines and fibers.")
    sleep(2)
    print("It pointed to the woman, her necklace, and the sound "
          "of howling wind and falling flora began to fill the air. "
          "The woman cried out;")
    print("'It's them! You idiot, they after this necklace! You've "
          "doomed us all!' Her face was pained, the necklace seeming "
          "to string outwards.")
    sleep(2)
    print("The necklace was struggling to go to the grasp of the "
          "middle figure, the howling growing louder by the second.")
    print("The medallion snaps off from the necklace and flies into "
          "the hands of the hooded Thing; the woman falling back "
          "down, immobile.")
    sleep(2)
    print("By now you see your limbs grow heavy and vision blurry. "
          "The figure now pointing to you; you turn to stone.")
    sleep(1)
    print("You chose an interesting end, didn't think you would "
          "come all this way just to turn around. Oh well!")
    dead()


def frontDoor():
    """This is a ploy trap I try to go through with our users to get
    them to lose; like an absolute meaner I am.
    __author__ = Daniel Claus Romeo
    """
    print("Almost as quickly as the doors swing open, you book it to "
          "the front door; crashing into it and nearly sending the "
          "door off the hinges.")
    sleep(1)
    print("Three hooded figures with foliage wrapped around "
          "themselves stand before you. The middle one raises its "
          "hand out to your bag.")
    print("You medallion tremors with the force of an earthquake and "
          "rips through your bag, into the hand of the hooded figure.")
    sleep(2)
    print("The figure, now grasping the necklace, starts to make a "
          "rustling sound similar to falling leaves from "
          "rushing wind.")
    print("The sound grows increasingly louder as each moment "
          "passes, and your vision starts to fade almost as quickly.")
    sleep(2)
    print("You've been turned into a statue, in the bottom of some "
          "'unknown place. The only thing you can do is think to "
          "yourself.")
    dead()


def path():
    """This is another end that I thought would bring about a
    cut-off for the story to end for the user.
    __author__ = Daniel Claus Romeo
    """
    print("You ignore the necklace and continue your walk.\nAs you "
          "walk the air becomes more arid and hotter in temperature.")
    sleep(1)
    print("It keeps climbing in temperature until you gain the sense "
          "to turn around.")
    print("But when you do, the trail you've known is just sand, same "
          "as what is around you as well.")
    sleep(2)
    print("Seems you've run into the old ' Walk until you reach sand '"
          " gag; but, without a good punch line.")
    print("You eventually succumb to your thirst.")
    sleep(2)
    print("Yikes! That was actually pretty weird. I wonder why the "
          "developer even made this an option if you were doomed to "
          "start.")
    dead()


def leave():
    """The first death I wrote for this code; puns and all.
    __author__ = Daniel Claus Romeo
    """
    print("You place it around your neck, you instantly transform "
          "into a fern; similar to the one you had just picked the "
          "necklace up from.")
    sleep(1)
    print("Seems your curiosity has led you done a green state you "
          "weren't quite expecting!")
    dead()


def left():
    """This side of the story is one of the less intense versions,
    but it was just as fun to write.
    __Author__ = Daniel Claus Romeo
    """
    print(
        "... you have just begun to feel you're walking into "
        "eternity when you see a T-junction. But just then you hear "
        "a  roar!!!")
    sleep(1)
    answer = input(
        "You turn back to see a giant lion, miles away, running after "
        "you at great speed. You just have time to react. \nDo you:\n("
        "1)dodge left?\n(2)or dodge right?")
    sleep(2)
    if answer == "1":
        dodgeLeft()
    elif answer == "2":
        dodgeRight()
    else:
        variableError()


def dodgeRight():
    """This is the intended choice for the player to take if they
    wish to progress within the 'left' story arc.
    __author__ = Daniel Claus Romeo"""
    sleep(3)
    answer = input(
        "After dodging right into a bush, completely avoiding the "
        "lion, you run for what seems like forever. Eventually, "
        "you end up finding a portal another dimension. Could this "
        "be a trap? Or should you take that chance?\nDo "
        "you:\n(1)Take said chance.\n(2)or do you continue on?")
    if answer == "1":
        chance()
    elif answer == "2":
        onward()
    else:
        variableError()


def onward():
    """This is the correct deviation to continue on with this arc of
    the story.
    __author__= Daniel Claus Romeo
    """
    print("You decide to do the sensible thing and not trust the "
          "mysteriously placed portal. Again, you begin your journey "
          "the dreaded woods.")
    sleep(2)
    print("You hear a whistle as something shoots up from a "
          "clearing, an object in clear view heading right for you.")
    sleep(1)
    answer = input("It's a dagger! It flies closer and closer with "
                   "each second.\nDo you:\n(1)allow it to strike "
                   "you\n(2)or do you obviously dodge?")
    if answer == "1":
        arrowToTheKnee()
    elif answer == "2":
        dodgeObv()
    else:
        variableError()


def dodgeObv():
    """"For proper continuation to the rest of this random arc,
    this decision is very necessary.
    __author__=Daniel Claus Romeo
    """
    print(
        "Leaping left, you dodge the strange looking knife. A few "
        "more come your way, allowing yourself even more dodges.")
    sleep(1)
    print(
        "As the last knife sticks into the ground, you catch a "
        "glimpse of the assassin. It's...Cthulu?!")
    sleep(1)
    print("The tentacled assassin meets before you in all his "
          "Love-craftian glory.")
    sleep(1)
    print("He speaks in 'blrrbss' and hisses, holding out his armed "
          "tentacle as if preparing for your retaliation.")
    sleep(1)
    answer = input("What do you do? Do you:\n (1) grab a nearby "
                   "knife and lunge at the God?\n(2) or do you "
                   "become the next sacrifice for this deity?")
    if answer == "1":
        lunge()
    elif answer == "2":
        sacrifice()
    else:
        variableError()


def lunge():
    """A simple end for a seemingly fitful end for the deity,
    yet a re-occurrence for the user.
    __author__= Daniel Claus Romeo
    """
    print("You go forth, knife in hand, thrusting it into the "
          "beard-like cluster of worm-like appendages.")
    sleep(1)
    print("With a gurgle and a spit of ink, your knife finds its new "
          "home within the breast of this beast.")
    sleep(1)
    print("A geyser of ink hits your face, sending you in a fit "
          "trying to clear your vision.")
    sleep(1)
    print(
        "Once you scrape away the effluence of this fearsome foe, "
        "you find yourself back at the beginning of the crossroads "
        "again.")
    sleep(2)
    print("Might as well give it another go, eh?")
    sleep(2)
    portalEnd()


def sacrifice():
    """An odd way to get through the rest of the story, but this
    entire left arc is pretty random compared to the other.
    __author__ = Daniel Claus Romeo
    """
    print("You recognize the strength of this Force, making yourself "
          "kneel in hopes to win some mercy.")
    sleep(1)
    print("Cthulu's posture changes, he lowers his 'arms', and makes "
          "his way over. He splurts out his ancient tongue while "
          "bringing his blade to your brow.")
    sleep(1)
    answer = input("In that moment, a chance brings itself once "
                   "more. He may be wanting to take your life still "
                   "and his grip seems loose on that knife. ""\nDo "
                   "you:\n(1)attempt to swipe the knife and use it as "
                   "leverage for escape.\n(2)or do you wait to see "
                   "what happens?")
    sleep(2)
    if answer == "1":
        badEnding()
    elif answer == "2":
        goodEnding()
    else:
        variableError()


def goodEnding():
    """A weirdly nice ending to the other, I enjoyed this half abit.
    __author__ = Daniel Claus Romeo
    """
    print("After allowing this God to say what he needed to say, "
          "strangely he holsters his blade and reached his arm out "
          "as if to help you up.")
    sleep(2)
    print("You stare blankly in disbelief; did you just become "
          "friends with one of the most mystically devious Lords of "
          "Destruction?")
    sleep(2)
    print("After helping you to your feet, he wraps his arm around "
          "your shoulder and seemingly smiles.")
    sleep(1)
    print("He 'squelches' some more phrases out and releases his"
          "'christian side-hug', walking away like nothing had ever "
          "happened.")
    sleep(2)
    print("Well, it seems you are now best friends with Cthulu; who "
          "at first was just testing your strength to see if you "
          "were strong enough become his friend at all.")
    sleep(2)
    print("You got the secret Good ending with Cthulu; you must be "
          "a really kind and trusting person. I commend you on your "
          "good-will.")
    sleep(2)
    print("In all honesty though, please don't try to befriend him "
          "if you ever do cross his path. I hear he punches babies "
          "and slaps puppies.")
    retry()


def badEnding():
    """I wanted to have two ways to end this weird story; in ways
    that could've only been imagined from this weird brain of mine.
    __author__ = Daniel Claus Romeo
    """
    print("You swiftly grab at the knife, stealing it from the slimy "
          "clutches of this Mad Lord.")
    sleep(1)
    print("The Creature furrows what would be its brow, trying to "
          "catch its balance after your grabbed its only weapon.")
    sleep(1)
    print("You jumped back, poised with malicious intent, and plunged "
          "the dagger into the eye of this Beast.")
    sleep(2)
    print("With an outcry of pain, Cthulu clutched his new wound and "
          "began to use his free hand to summon a portal.")
    sleep(1)
    print("As he fled, you felt a sense of relief. You just stabbed "
          "a God...Woah..")
    sleep(1)
    print("I know I'm just the narrator, but that was pretty cool! "
          "I'm sure there will be no repercussions for that...I hope.")
    sleep(2)
    print("You got the darker, less secret, ending with your encounter"
          "with Cthulu!")
    sleep(1)
    print(
        "Now that you've done the left side, try again and go right.")
    sleep(1)


def arrowToTheKnee():
    """For this one, it was more fun to make a comical reference to
    the Game 'Skyrim's arrow to the knee joke.
    __author__= Daniel Claus Romeo and Bethesda for the reference.
    """
    print(
        "You open your arms comically and allow this blade to make "
        "its impact; strangely it only embeds itself into your knee.")
    sleep(2)
    print("The searing pain that this knee sent throughout your body "
          "also strangely brings about a thought that you are done "
          "with adventuring.")
    print("It seems to have also been laced with a toxin; as your "
          "eyes fog and your vision fades.")
    sleep(2)
    print("Man, you know I used to be an adventurer just like you.")
    dead()


def chance():
    """This segment allows for the segment where the user will end
    up with another death scene
    __author__= Daniel Claus Romeo
    """
    print("You decided to dive straight though the portal; a "
          "similar road flashes into view after you get up on your "
          "feet.")
    sleep(2)
    print("You have been walking for miles... and this is getting "
          "frustrating. Will this road ever end?")
    sleep(1)
    print("Soon you come to a path; one that seems all too "
          "familiar...Oh NOO! You're back at the start..")
    sleep(1)
    portalEnd()


def dodgeLeft():
    """"This function brings about a dead end/death scene for if you
    chose the first choice in the previous function.
    __author__ = Daniel Claus Romeo"""
    print(
        "Unfortunately for you, the lion catches up and rips you to "
        "shreds. You feel intense pain, yet think it pretty cool to "
        "have died from such a beast.")
    sleep(1)
    dead()


def portalEnd():
    print("You seem to have gone back to the very beginning; why "
          "don't you try again?")
    sleep(2)
    retry()


def dead():
    """Before the answer for the function 'adventure()' turns false and
    ends I've made the choice to go ahead and add these to print
    statements so that the users have an ending for their demise.
    __author__= Daniel Claus"""

    print(
        "It seems you have met an untimely end," + name + " I "
                                                          "implore "
                                                          "you to "
                                                          "try again!")
    sleep(1)
    print("Thanks for playing!")
    sleep(1)
    retry()


def retry():
    """I created this function so that it may politely ask the user
    if they want to try again; if not, it will break the loop and
    end the game.
    __author__ = Daniel Claus
    """
    answer = input("Would you like to play again?\n(1)Yes\n(2)No")
    if answer == "1":
        intro()
    elif answer == "2":
        print("Well..Fine! It's not like i was programmed to do "
              "anything else. Enjoy restarting the file again "
              "you very mean user.")
        sleep(1)


def win():
    print(" Congratulations! You've done the weird honor of beating "
          "this game!")
    sleep(1)
    retry()


def variableError():
    print(
        "You need to choose either (1) or (2). Please do give it "
        "another shot! ")
    sleep(3)
    retry()


intro()
