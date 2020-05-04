#hangman v2 by Joon Hao, build in Visual Studio Code, with Python 3

import time, random

#variables
game = True
word = "Extravagant"
round = 10


while game:
    #intro
    print("Welcome to hangman v2.")
    time.sleep(1.5)
    print("Let's see if you can figure that lucky word.")
    print()
    print()
    time.sleep(2)


    #instructions
    print("Instructions for this game:\n1. You are to guess the word in 10 tries\n2. You are allowed to guess the letters of the lucky word 9 times.\n3. The last try, you would have to guess the word, if not, I (the host) win!")
    print()
    time.sleep(3.5)


    #Game starting
    print()
    print("Ready!")
    time.sleep(1)
    print("Set!")
    time.sleep(1)
    print("GO!")
    time.sleep(1)
    print()
    print()
    
    #game 
    print("The lucky word is a 11 letter word, adjective\nmeaning: lacking restraint in spending money or using resources.")
    word_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    while round > 1:
        round = round - 1
        guess = input("guess: ")

        #analysis
        if guess == "e" or guess == "E":
            word_game[0] = "E"
            print(word_game)
            print()

        elif guess == "x" or guess == "X":
            word_game[1] = "x"
            print(word_game)
            print()

        elif guess == "t" or guess == "T":
            word_game[2] = "t"
            word_game[10] = "t"
            print(word_game)
            print()

        elif guess == "r" or guess == "R":
            word_game[3] = "r"
            print(word_game)
            print()

        elif guess == "a" or guess == "A":
            word_game[4] = "a"
            word_game[6] = "a"
            word_game[8] = "a"
            print(word_game)
            print()

        elif guess == "v" or guess == "V":
            word_game[5] = "v"
            print(word_game)
            print()

        elif guess == "g" or guess == "G":
            word_game[7] = "g"
            print(word_game)
            print()

        elif guess == "n" or guess == "N":
            word_game[9] = "n"
            print(word_game)
            print()

        else:
            print("Nope, there isn't a " + guess + " in the lucky word.")
            time.sleep(2)
            print()

        #attempts left str
        print("You left " + str(round) + " attempts!")

    
    #last round
    if round == 1:
        round = round - 1
        print("Last attempt, time to guess your word!")
        time.sleep(2)
        guess_word = input("What is the word?\n")

        #analysis
        if guess_word == "Extravagant" or guess_word == "extravagant":
            print()
            print("Once again you beat me. Congrates!")
            time.sleep(3.5)

        else:
            print()
            print("Oops, seems like you guessed it wrong :(")
            time.sleep(2.5)

        #user choice to restart
        user_restart = input("Do you want to play again? (y/n)\n")
        if user_restart == "y" or user_restart == "Y":
            round = 10
            print()
            print('**************************************')
            print()
            game == True
            
        
        elif user_restart == "n" or user_restart == "N":
            print("Bye, bye.")
            print()
            print("Hangman v2 by Joon Hao, build in Visual Studio Code with Python 3.")
            game == False
            break

        else:
            user_restart = input("Sorry, I didn't get you there. Please reply with y/n")

    else:
        pass