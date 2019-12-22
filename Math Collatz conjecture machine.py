#Math Collatz cojecture machine by Joon Hao, built in Visual Studio Code, with python 3



#formula: even / 2,  odd * 3 + 1

#import
import time, random


#intro
print("Welcome to math collatz conjecture machine!")
print()
print()
time.sleep(3)


#instructions
print("Instruction:\n1. You are to input any number and wait for the result!")
print()
print()
time.sleep(3)



#start
l = input("Enter a number: ")
l = int(l)
i = [l]
def collatz(n):
    print(i)
    if n==1:
        return i
    if n%2 == 0:
        n = n/2
        i.append(n)
        return collatz(n)
    else:
        n = ((n*3) + 1)
        i.append(n)
        return collatz(n)
collatz(l)








