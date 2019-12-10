#Scissors, paper, stone version 2.0. Created by Joon Hao, built in Visual Studio Code, with Python 3.

import time, random

#variables
computer_weapon_number = random.randint(1, 3)
round_number = 0
user_score = 0
computer_score = 0


#Intro
print("Welcome to another game of scissors, paper, stone with computer!")
time.sleep(3)
print("This time you will be the one who selects one of the weapon and fighting with the computer itself!")
print("How cool will that be!?!?")
time.sleep(6)


#instructions
print()
print()
print("Instructions for this game: \n1. The player (you & computer) that has the most point after 10 rounds win! \n2. The rules of scissors, paper, stone apllys to this game (duh)")
time.sleep(6)


#Game about to start
print()
print()
user_name = input("First, what is your name?")
print()
print()
user_ready = input("The game is about to start, are you ready?")


#Game in progress
if user_ready == "Yes" or user_ready == "yes" or user_ready == "Y" or user_ready == "y":
    print("That is what I wanted to hear. \nLet's go!")
    time.sleep(3.5)

    #Game started
    while round_number <10:
        round_number = round_number + 1
        user_choice_number = input("Please choose one weapon (type the number corresponding to the weapon of choice): \n1. Scissors \n2. Paper \n3. Stone")

        #User choice from number to word
        if user_choice_number == "1":
            user_choice_word = "Scissors"
        elif user_choice_number == "2":
            user_choice_word = "Paper"
        else:
            user_choice_word = "Stone"


        #user's input
        print(user_name + " chose: " + user_choice_word)
        time.sleep(1)
        print("Now is computer's turn...")
        time.sleep(4)
        print()

        #computer's input
        computer_weapon_number = random.randint(1, 3)

        if computer_weapon_number == 1:
            computer_weapon_word = "Scissors"
        elif computer_weapon_number == 2:
            computer_weapon_word = "Paper"
        else:
            computer_weapon_word = "Stone"

        print("Computer choice is " + computer_weapon_word)
        time.sleep(3)
        print()

        print(user_name + ":" + " " + user_choice_word + "   " + "vs" + "   " + "Computer: " + computer_weapon_word)
        time.sleep(2)
        print()
        print()

        if user_choice_number == "1" and computer_weapon_number == 2:
            print("Congratulations " + user_name + ", you win this round!")
            user_score = user_score + 1
        elif user_choice_number == "1" and computer_weapon_number == 3:
            print("Sadly, computer win this round.")
            computer_score = computer_score + 1
        elif user_choice_number == "2" and computer_weapon_number == 1:
            print("Sadly, computer win this round.")
            computer_score = computer_score + 1
        elif user_choice_number == "2" and computer_weapon_number == 3:
            print("Congratulations " + user_name + ", you win this round!")
            user_score = user_score + 1
        elif user_choice_number == "3" and computer_weapon_number == 1:
            print("Congratulations " + user_name + ", you win this round!")
            user_score = user_score + 1
        elif user_choice_number == "3" and computer_weapon_number == 2:
            print("Sadly, computer win this round.")
            computer_score = computer_score + 1
        else:
            print("Tie!")

    if computer_score == 10 or user_score == 10:
        time.sleep(3)
        print()
        print()
        print("The game has ended!")

    time.sleep(2)

    #results
    if user_score > computer_score:
        print("Congratulations " + user_name + ", you defeated computer in this game!")
        time.sleep(5)
        print()
        print("Final scores:")
        print(user_name + ": " + user-score)
        print("Computer: " + computer_score)
    elif user_score < computer_score:
        print("Unfortunately, you lost to computer :(")
        time.sleep(5)
        print()
        print("Final scores:")
        print(user_name + ": " + user-score)
        print("Computer: " + computer_score)
    else:
        print("Seems like is a tie...")
        time.sleep(5)
        print()
        print("Final scores:")
        print(user_name + ": " + user-score)
        print("Computer: " + computer_score)


#User not ready
elif user_ready == "No" or user_ready == "no" or user_ready == "N" or user_ready == "n":
    print("Oh ok. Than I will be heading back. \nWhen you are ready, re-run the kernal(code).")



#Outro
time.sleep(5)
print("Thank you for playing this game. \nGame created by Joon Hao \nBuilt in Visual Studio Code \nWith Python 3")
