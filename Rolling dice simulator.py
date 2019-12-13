#Rolling dice simulator by Joon Hao, built in Visual Studio Code, with Python 3

#import
import time, random

#Intro
print("Welcome to rolling dice simulator!")
print()
print()
time.sleep(3)


#rollling dice
user_dice_yn = input("Would you like to roll the dice? ")

if user_dice_yn == "yes" or user_dice_yn == "Yes" or user_dice_yn == "y" or user_dice_yn == "Y":
    print()
    print("Rolling the dice!")
    print()
    print()
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print("Dice 1: " + str(dice_1))
    print("Dice 2: " + str(dice_2))
elif user_dice_yn == "no" or user_dice_yn == "No" or user_dice_yn == "n" or user_dice_yn == "N":
    print()
    print("Ok, seems like I am not going to roll the dice...")
else:
    print("Please re-run the programme and reply the question with yes or no")


print("Thank you for using this programme")
print("Created by Joon Hao, built in Visual Studio Code, with Python 3")
