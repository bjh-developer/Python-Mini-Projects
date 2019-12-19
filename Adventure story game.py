#Adventure story game by Joon Hao, built in Visual Studio Code, with Python 3

#import
import time

#Intro
print("Welcome to adventure story game!")
print()
print()
time.sleep(3)

#instructions
print("Instructions for this game:\n1. You will be given the option to control what you want the character to do next\n2. You can re-run the programme to complete all endings")
print()
print()
time.sleep(3)

#choose player
user_name = input("First, type in your player's name: ")
print()
time.sleep(1)
print("Let's go! Teleporting to another dimension...")
time.sleep(4)

#Game starts
print()
print()
print()


#1st chapter
print(user_name + " is now walking down the trail. You are surrounded by bushes and huge trees.")
print("All of the sudden, you spotted something moving in the bushes.")
print("What would you do?\n1. Go nearer the object\n2. Walk away")
user_choice_1 = input("Your choice: ")

if user_choice_1 == "1" or user_choice_1 == "Go nearer the object" or user_choice_1 == "go nearer the object":
    print("BOOOO! You got scared and fainted. Seems like today is not your day :( [Ending number 1]")
else:
    print("You slowly by steadily walked away from the object, not wanting to risk your life. Maybe that's a good choice... who knows?")
    print("Down the street, you saw an antique house. You know that someone is in there because there is smoke coming out from the chimney.")
    print("What would you do?\n1. Go into the house\n2. Walk pass it")
    user_choice_2 = input("Your choice: ")

    if user_choice_2 == "2" or user_choice_2 == "Walk pass it" or user_choice_2 == "walk pass it":
        print("You are so boring...")
        print("But seems like you made a wrong choice...")
        print("While you are walking, a kidnaper caught you and killed you... Bye Bye [Ending number 2]")
    else:
        print("Slowly walking up the stairs leading up to the house door, you saw a sign saying 'Don't enter!'")
        print("You hesitated")
        print("What would you do?\n1. Knock the door\n2. Open the door without knocking")
        user_choice_3 = input("Your choice: ")

        if user_choice_3 == "1" or user_choice_3 == "Knock the door" or user_choice_3 == "knock the door":
            print("Suddenly, you felt something behind you. You turned around and OOF. You just got slashed by a knife. So Sad... [Ending number 3]")
        else:
            print("You pushed open the door and to your surprise, you saw a treasure chest right in front of you.")
            print("What would you do?\n1. Open it up\n2. Ignore it")
            user_choice_4 = input("Your choice: ")

            if user_choice_4 == "1" or user_choice_4 == "Open it up" or user_choice_4 == "open it up":
                print("BOOOO! You got a shock of your life seeing hundreds of spiders crawling out and you fainted. What a tragic way to die... [Ending number 4]")
            else:
                print("You walk into the house and saw an old man sitting at the fireplace. You slowly walk up and the old man turned around, staring at you.")
                print("The old man took up his gun and before you knew it, you are dead... [Ending number 5, last story]")


print("If you managed to get to the last, congrats. You can try again for fun :)")
time.sleep(3)
print()
print()
print("Thank you for playing this game. Created by Joon Hao, Built in Visual Studio Code, With Python 3")
