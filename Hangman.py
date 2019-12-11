#Hangman game by Joon Hao, built in Visual Studio Code, with Python 3.

#import
import time, random


#variables
word = "Hashbrown"
round_number = 7


#intro
print("Welcome to a game of Hangman!")
time.sleep(3)
print("I am the host, Joon Hao. \nAnd today, I will challenge you to a round of hangman!")
time.sleep(3.5)


#Instructions
print()
print()
print("Instructions for this game: \n1. You are to guess the lucky word within 7 tries.\n2. You are allowed to guess the letters of the lucky word 6 times.\n3. The last try, you would have to guess the word, if not, I (the host) win!")
time.sleep(5.5)
print()
print()


#Game starting
print("Ready, get set, GO!")
time.sleep(2)
print()
print()

#Game in progress
time.sleep(2)
print("The lucky word has 9 letters in it and it is related to food.")
while round_number > 1:
    round_number = round_number - 1
    user_1_guess = input("What letter you want to guess? ")
    print("You guess " + user_1_guess)

    if user_1_guess == "h":
        print("There are 2 'h'")
        print("Lucky word: H _ _ h _ _ _ _ _")
        time.sleep(2)
        print()
    elif user_1_guess == "a":
        print("There is 1 'a'")
        print("Lucky word: _ a _ _ _ _ _ _ _")
        time.sleep(2)
        print()
    elif user_1_guess == "s":
        print("There is 1 's'")
        print("Lucky word: _ _ s _ _ _ _ _ _")
        time.sleep(2)
        print()
    elif user_1_guess == "b":
        print("There is 1 'b'")
        print("Lucky word: _ _ _ _ b _ _ _ _")
        time.sleep(2)
        print()
    elif user_1_guess == "r":
        print("There is 1 'r'")
        print("Lucky word: _ _ _ _ _ r _ _ _")
        time.sleep(2)
        print()
    elif user_1_guess == "o":
        print("There is 1 'o'")
        print("Lucky word: _ _ _ _ _ _ o _ _")
        time.sleep(2)
    elif user_1_guess == "w":
        print("There is 1 'w'")
        print("Lucky word: _ _ _ _ _ _ _ w _")
        time.sleep(2)
        print()
    elif user_1_guess == "n":
        print("There is 1 'n'")
        print("Lucky word: _ _ _ _ _ _ _ _ n")
        time.sleep(2)
        print()
    else:
        print("Nope, there isn't a " + user_1_guess + " in the lucky word.")
        time.sleep(2)
        print()

    print("You left " + str(round_number) + " attempts!")


while round_number == 1:
    round_number = round_number - 1
    print("You are on your last attempt, means that you have to guess the word now.")
    time.sleep(3)
    print()
    user_ans = input("So, what is the lucky word? ")
    if user_ans == "Hashbrown" or user_ans == "hashbrown":
        print()
        print()
        print("Congratulations, you guessed it right. You seem pretty smart. I will be back to take my revenge!")
        time.sleep(5)
    else:
        print()
        print()
        print("Oops, seems like you guessed it wrong :(")
        print("If you want to try again, re-run the kernel. (Don't worry, the lucky word will stay the same)")
        time.sleep(5)



#Outro
print()
print()
print()
print("Thank you for playing this game!")
print("Created by Joon Hao, built in Visual Code Studio, with Python 3")