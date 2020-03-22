#Calendar by Joon Hao, built in Visual Studio code, with Python 3

#import
import calendar, time

#intro
print("Welcome to Calendar")
print()
print()

#start
while True:
    user_choice = input("Enter 'quit' to exit programme\nEnter 'fun fact' to find out if it is a leap year!\nEnter 'year' to see calendar for the year\nEnter 'month to see calendar for the month\n:")

    #fun fact
    if user_choice == "fun fact" or user_choice == "Fun fact" or user_choice == "Fun Fact":
        print()
        print()
        year = input("Year for fun fact: ")
        is_leap = calendar.isleap(int(year))

        #not leap
        if is_leap == "false":
            print()
            print(year + " is not a leap year")
            print()
            print()

        #leap
        else:
            print()
            print(year + " is a leap year!")
            print()
            print()

    #see year calendar
    elif user_choice == "year" or user_choice == "Year":
        print()
        print()
        year = input("Year: ")
        print()
        print(calendar.calendar(int(year)))

    #see month calendar
    elif user_choice == "month" or user_choice == "Month":
        print()
        print()
        year = input("Year: ")
        month = input("Month (in number): ")
        print()
        print(calendar.month(int(year), int(month)))

    #user quit programme
    elif user_choice == "quit" or user_choice == "Quit":
        print("Closing programme...")
        time.sleep(2)
        print("Good bye!")
        break

    #unknown user input
    else:
        print("Unknown input. please try again")