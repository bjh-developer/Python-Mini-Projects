#HCF and LCM finder created by Joon Hao, in Visual Studio Code with Python 3

import time, random, math, cmath


print("Welcome to HCF and LCM Finder developed by Joon Hao!")
time.sleep(2)

while True:
    print()
    print("Enter 'quit' to exit programme")
    print()
    print("Would you like to find HCF or LCM?")
    user_HCF_LCM = input(":")

    if user_HCF_LCM == "LCM" or user_HCF_LCM == "lcm":
        def compute_lcm(x, y):

            if x > y:
                greater = x
            else:
                greater = y

            while True:
                if((int(greater) % int(x) == 0) and (int(greater) % int(y) == 0)):
                    lcm = greater
                    break
                greater += 1

            return lcm

        num1 = input("First number: ")
        num2 = input("Second number: ")

        lcm = compute_lcm(int(num1), int(num2))
        print("The LCM is " + str(lcm))

    elif user_HCF_LCM == "HCF" or user_HCF_LCM == "hcf":
        def compute_hcf(x, y):
            while(y):
                x, y = y, x % y
            return x

        num1 = input("First number: ")
        num2 = input("Second number: ")

        hcf = compute_hcf(int(num1), int(num2))
        print("The HCF is " + str(hcf))

    elif user_HCF_LCM == "quit" or user_HCF_LCM == "Quit":
        print("Shutting down programme...")
        time.sleep(2)
        print("Good bye!")
        break
        
    else:
        print("Unknown input, please try again...")