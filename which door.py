#"which door?" by Joon Hao, built in Visual Studio code, with Python

import time
import random

game = True

while game:

    print("Investigator Lee: Hello and welcome to your first day of work.")
    time.sleep(2)
    print()
    user_name = input("First, what is your name: ")
    print("Investigator Lee: Interesting name you got there " + user_name)
    time.sleep(1.5)
    print()
    print("Investigator Lee: Since today is your first day, I will be walking you through how we do our work here...")
    time.sleep(3.5)
    print()
    print("System PA: CODE RED! CODE RED! INTRUDER ALERT! INTRUDER ALERT")
    time.sleep(2)
    print()
    print("Investigator Lee: Erm... never mind, you go help me get the keys and I will come look for you, just get the keys from the doors, NOW!")
    time.sleep(4)

    #start of game
    door_blue = "blue, 1234"
    door_red = "red, 2134"
    door_white = "white, 4231"

    print()
    print()
    print()
    print()
    print("Narrator: There are three doors (blue, red, white) in front of you and you are to figure the right door and the right password to retrieve the key.")
    time.sleep(2)
    print()
    print("Narrator: Read the following passage to figure out the door colour and password, good luck, you have 2 tries.")
    time.sleep(4)
    print()
    print()
    print("I have never seen such a rare fish before!, it is blue and has shiny fins! This must cost a lot, let me check the price of this fish... OMG! It cost $1234!! Not the most expensive though... Anyway what am I here for? Ah yes, to see the cost of the blueberries and maybe buy one box of it to be able to get the key experience of eating blueberries for some reason.")
    time.sleep(10)
    print()
    user_guest = input("Narrator: So, have you figured out what door colour and the password is? Type it in the following order(colour, password)\n")


    if user_guest == door_blue:
        print("Hooray! You got the right combination! Now take the key and give it to inspector Lee!")
        time.sleep(3)
        print()
        print("Congratulations, you have passed round 1. Stay tune for more rounds...")
        print("This is narrator signing off...")
        user_end = input("Would you like to try again?")

        #restart game
        if user_end == "Yes" or user_end == "yes" or user_end == "y" or user_end == "Y":
            game == True

        #end game
        elif user_end == "No" or user_end == "no" or user_end == "n" or user_end == "N":
            game == False
            print("Thank you for playing this game")
            print("This game is built by Joon Hao in Visual Studio Code with Python 3")
            break

        else:
            print("Sorry, I didn't get it, can you type again?")

    elif user_guest != door_blue:
        print("That's incorrect... you left last try")
        user_guest = input("")

        if user_guest == door_blue:
            print("Hooray! You got the right combination! Now take the key and give it to inspector Lee!")
            time.sleep(3)
            print()
            print("Congratulations, you have passed round 1. Stay tune for more rounds...")
            print("This is narrator signing off...")
            print()
            user_end = input("Would you like to try again?")

            #restart game
            if user_end == "Yes" or user_end == "yes" or user_end == "y" or user_end == "Y":
                game == True

            #end game
            elif user_end == "No" or user_end == "no" or user_end == "n" or user_end == "N":
                game == False
                print("Thank you for playing this game")
                print("This game is built by Joon Hao in Visual Studio Code with Python 3")
                break

            else:
                print("Sorry, I didn't get it, can you type again?") 

        else:
            print("Nope. Bye bye\nYou DIED.")
            user_end = input("Would you like to try again?")

            #restart game
            if user_end == "Yes" or user_end == "yes" or user_end == "y" or user_end == "Y":
                game == True

            #end game
            elif user_end == "No" or user_end == "no" or user_end == "n" or user_end == "N":
                game == False
                print("Thank you for playing this game")
                print("This game is built by Joon Hao in Visual Studio Code with Python 3")
                break

            else:
                print("Sorry, I didn't get it, can you type again?") 

    else:
        print("Error, please contact owner to debug")
        break