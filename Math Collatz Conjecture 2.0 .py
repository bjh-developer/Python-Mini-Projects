#Math Collatz cojecture machine 2.0 by Joon Hao, built in Visual Studio Code, with python 3



#formula: even / 2,  odd * 3 + 1

#import
import time, random


#intro
print("Welcome to math collatz conjecture machine!")
print()
print()
time.sleep(3)


#instructions
print("Instruction:\n1. Just wait for the results and you will be surprised!")
print()
print()
time.sleep(3)

print("Starting in")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")
print()
print()


#start
l = random.randint(2, 1000000)
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

