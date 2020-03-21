#countdown timer created by Joon Hao, in Visual Studio code with Python 3

#import modules
import time

#intro
print("Welcome to countdown timer!")
print()
print()

#start
while True:
    print("Enter 'quit' to exit programme\nEnter 'countdown' to start countdown from specified time")
    user_choice = input(":")

    #user's choice
    if user_choice == "quit" or user_choice == "Quit":
        print("Closing programme...")
        time.sleep(2)
        print("Good bye!")
        break

    elif user_choice == "countdown" or user_choice == "Countdown":
        time_sec = input("Time(sec): ")
        print("Starting countdown")
        print()
        print(time_sec)

        #negative not accepted message
        if int(time_sec) < 0:
                print("That's a negative! You can't turn back time!\nTry again")
                print()
                print()
        else:
            pass

        #start countdown
        while int(time_sec) > 0:
            time_sec = int(time_sec) - 1
            time.sleep(1)
            print(time_sec)

            #end message
            if time_sec == 0:
                print("Time's UP!!!")
            else:
                pass
            
    #user error message
    else:
        print("Unknown input, please try again")