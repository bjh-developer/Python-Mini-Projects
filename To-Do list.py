#To-Do list by Joon Hao, build in Visual Studio Code, with Python 3

#import
import time

#variables
program = True
todolist = []

#intro
print("Hello there")
time.sleep(2)
print("Below is your to-do list.")

#todo start
while program:
    time.sleep(2)
    print("You have " + str(len(todolist)) + " things to do!")

    #check number of to-do
    if len(todolist) == 0:
        print()
        print("Yay! Nothing to do!")

    else:
        pass

    print()
    print(todolist)
    print()
    user_action = input("What do you want to do? (Add / Delete / Done / Quit)\n")
    print()

    #user action
    if user_action == "Add" or user_action == "add":
        user_item_add = input("What do you need to do: ")
        todolist.append(user_item_add)
        print()
    
    #user delete
    elif user_action == "Delete" or user_action == "delete":
        user_item_del = input("What do you want to remove (type exactly): ")

        if user_item_del not in todolist:
            print()
            print("Oops, it seems like the item is not in your to-do list, please check your spelling")
            print()
            time.sleep(2.5)

        else:
            todolist.remove(user_item_del)

        print()
    
    #user done
    elif user_action == "Done" or user_action == "done":
        user_item_done = input("What are you done with (type exactly): ")

        if user_item_done not in todolist:
            print()
            print("Oops, it seems like the item is not in your to-do list, please check your spelling")
            print()
            time.sleep(2.5)

        else:
            todolist.remove(user_item_done)
            print(user_item_done + " done ✔" + "\nKeep it up!")
        
        print()

    #user quit program
    elif user_action == "Quit" or user_action == "quit":

        if len(todolist) == 0:
            print("You finished everything! It is time to relax...")
            time.sleep(2)
        
        else:
            print("You left " + str(len(todolist)) + " more things to do, but you deserve a break...")
            time.sleep(2)

        print("Good Bye!")
        print("To-Do list by Joon Hao, built in Visual Studio Code with Python 3")
        program == False
        break

    #user typo
    else:
        print("Sorry, I didn't get what you mean, please try again...")
        print()
        time.sleep(2.5)