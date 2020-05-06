#date counter by Joon Hao, built in Visual Studio Code, with Python 3

#import
import time, random, datetime, pytz

#variables
counter = True

#intro
print("Welcome to date counter")
time.sleep(2)
print()

#start
while counter:

    user_mode = input("Please select a mode ('quit' to exit program):\n1. days since birth\n2. days to birthday\n3. days to new year!\n4. date & time now\n")
    print()

    #days since birth counter
    if user_mode == "1":
        print("Type in the year, month and day you were born on")
        print()
        user_year = input("Year: ")
        user_month = input("Month: ")
        user_day = input("Day: ")
        user_birthday = datetime.date(int(user_year), int(user_month), int(user_day))
        today = datetime.date.today()
        days_since_birth = (today - user_birthday).days
        print()
        print("Days since you were born: " + str(days_since_birth))
        time.sleep(2)
        print()
        print()


    #days to birthday
    elif user_mode == "2":
        print("Type in the year, month and day your next birthday is on")
        print()
        user_year = input("Year: ")
        user_month = input("Month: ")
        user_day = input("Day: ")
        user_next_birthday = datetime.date(int(user_year), int(user_month), int(user_day))
        today = datetime.date.today()
        days_to_birthday = (user_next_birthday - today).days
        print()
        print("Days to your birthday: " + str(days_to_birthday))
        print("Happy birthday in advance (" + str(days_to_birthday) + " days)")
        time.sleep(2)
        print()
        print()

    #days to new year
    elif user_mode == "3":
        print("Type in the year, month and day currently")
        #user year
        now_year = input("Year (now): ")
        #user month
        now_month = input("Month (now): ")
        #user day
        now_day = input("Day (now): ")
        #now
        user_now = datetime.date(int(now_year), int(now_month), int(now_day))
        #next year
        next_year = int(now_year) + 1
        user_next = datetime.date(int(next_year), 1, 1)
        #days to new year
        day_to_new_year = (user_next - user_now).days
        print()
        print("You are " + str(day_to_new_year) + " more day to " + str(next_year) + "!")
        time.sleep(1)
        print("Use your time wisely")
        time.sleep(2)
        print()
        print()

    #time zone
    elif user_mode == "4":
        datetime_today = datetime.datetime.now(tz=pytz.UTC)
        datetime_sg = datetime_today.astimezone(pytz.timezone('Asia/Singapore'))
        print("The current date & time in Singapore is " + str(datetime_sg) + ", time zone: Asia/Sinagpore GMT-8")
        time.sleep(2)
        print()
        print()

    #end
    elif user_mode == "quit" or user_mode == "Quit":
        print("Goodbye!\nShutting program...")
        time.sleep(2)
        print("date counter created by Joon Hao, built in Visual Studio Code with Python 3")
        counter = False
        break

    #error
    else:
        print()
        print("Sorry, I didn't get it, please enter the corresponding numbers that you want the counter to do or enter 'quit' to exit.")
        time.sleep(2)
        print()