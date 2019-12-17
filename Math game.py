#Math game by Joon Hao, built in Visual Studio Code, with Python 3



#import
import time


#Intro
print("Welcome to Math game!")
print()
print()
time.sleep(2)

#instructions
print("Instructions for this game:\n1. You will be allowed to choose the type of math question you would like to answer.\n2. When you want to exit, type 'exit'\n3. Try to get all correct!")
print()
print()
time.sleep(5)


#Game starts
user_score = 0
no_questions = 0

while no_questions < 5:
    print()
    time.sleep(1)
    print("***************************")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5.Impossible math")
    user_choice = input("What type of questions would you like to answer? ")
    print("***************************")
    no_questions = no_questions + 1

    if user_choice == "Addition" or user_choice == "addition" or user_choice == "1":
        print("Answer this question:\n197085 + 2309 = ___")
        user_ans_1 = input("What is your answer? ")
        
        if user_ans_1 == "199394":
            print("Correct!")
            user_score = user_score + 1
        elif user_ans_1 == "exit" or user_ans_1 == "Exit":
            break
        else:
            print("Incorrect")
    elif user_choice == "Subtraction" or user_choice == "subtraction" or user_choice == "2":
        print("Answer this question:\n90020 - 12345 = ___")
        user_ans_2 = input("What is your answer? ")

        if user_ans_2 == "77675":
            print("Correct!")
            user_score = user_score + 1
        elif user_ans_1 == "exit" or user_ans_1 == "Exit":
            break
        else:
            print("Incorrect")
    elif user_choice == "Multiplication" or user_choice == "multiplication" or user_choice == "3":
        print("Answer this question:\n12345 * 12 = ___")
        user_ans_3 = input("What is your answer? ")

        if user_ans_3 == "148140":
            print("Correct!")
            user_score = user_score + 1
        elif user_ans_1 == "exit" or user_ans_1 == "Exit":
            break
        else:
            print("Incorrect")
    elif user_choice == "Division" or user_choice == "division" or user_choice == "4":
        print("Answer this question:\n8244 / 12 = ___")
        user_ans_4 = input("What is your answer? ")
        
        if user_ans_4 == "687":
            print("Correct!")
            user_score = user_score + 1
        elif user_ans_1 == "exit" or user_ans_1 == "Exit":
            break
        else:
            print("Incorrect")
    else:
        print("Answer this Impossible Question:\n123456789 * 123456789 / 9807060504030201 + 1029384756 - 121314151617181910")
        user_ans_5 = input("What is your answer? ")

        if user_ans_5 == "-1.2131415e+17":
            print("You must have used the calculator\nbut you still got it thanks to the calculator\ncount you smart")
            user_score = user_score + 1
        elif user_ans_1 == "exit" or user_ans_1 == "Exit":
            break
        else:
            print("At least you never use calculator... or did you? Hmmmmmmmm\nIncorrect")


time.sleep(3)
print()
print()
print("Thank you for playing this math game!")
print("Your finale score is " + str(user_score) + " out of 5")
print()
time.sleep(2)
print("If you got all correct, congrates yourself!\nIf not, don't worry:(")
print()
print()
print("Game created by Joon Hao, built in Visual Studio Code, with Python 3")
