#Scissors, paper, stone game by Joon Hao using Python 3 on Thonny IDE

import random, time

#variables
computer1_weapon = random.randint(1, 3)
computer2_weapon = random.randint(1, 3)
computer1_score = 0
computer2_score = 0



#intro
print("Welcome to a game of...")
time.sleep(2)
print("scissors")
time.sleep(1)
print("paper")
time.sleep(1)
print("stone")
print()
print()

#instructions
time.sleep(3)
print("Instructions for this game:")
print()
print("1. The computer with the highest points after 10 rounds is the winner")
print()
print("2. You cannot decide who win since is all based on luck and the computer:) (but at least you get to decide the name...)")
print()
print("3. In this game, 1 = Scissors, 2 = Paper, 3 = Stone")
print()
print()
print()



#game
time.sleep(5)
print("Let the game begins!")

time.sleep(2)


#name of C1/C2
C1_name = input("Name of computer 1?")
C2_name = input("Name of computer 2?")
print()
print()
print()


#game starting
print("Game starting in")
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
print()


#Game progress
round_number = 0


while round_number < 10:
    round_number = round_number + 1
    computer1_weapon = random.randint(1, 3)
    computer2_weapon = random.randint(1, 3)
    print(C1_name + ":" + str(computer1_weapon))
    print(C2_name + ":" + str(computer2_weapon))
    
    if computer1_weapon == 1 and computer2_weapon == 1:
        print("Tie!")
        print()
        time.sleep(1)
    elif computer1_weapon == 1 and computer2_weapon == 2:
        print(C1_name + " wins this round!")
        print()
        time.sleep(1)
        computer1_score = computer1_score + 1
    elif computer1_weapon == 1 and computer2_weapon == 3:
        print(C2_name + " wins this round!")
        print()
        time.sleep(1)
        computer2_score = computer2_score + 1
    elif computer1_weapon == 2 and computer2_weapon == 2:
        print("Tie!")
        print()
        time.sleep(1)
    elif computer1_weapon == 2 and computer2_weapon == 1:
        print(C2_name + " wins this round!")
        print()
        time.sleep(1)
        computer2_score = computer2_score + 1
    elif computer1_weapon == 2 and computer2_weapon == 3:
        print(C1_name + " wins this round!")
        print()
        time.sleep(1)
        computer1_score = computer1_score + 1
    elif computer1_weapon == 3 and computer2_weapon == 3:
        print("Tie!")
        print()
        time.sleep(1)
    elif computer1_weapon == 3 and computer2_weapon == 1:
        print(C1_name + " wins this round!")
        print()
        time.sleep(1)
        computer1_score = computer1_score + 1
    elif computer1_weapon == 3 and computer2_weapon == 2:
        print(C2_name + " wins this round!")
        print()
        time.sleep(1)
        computer2_score = computer2_score + 1
    else:
        print("ERROR : statement else printed.")
        print("Seems like there is a problem if you see this message, please inform Joon Hao about this bug:(")
        print()
        time.sleep(0.5)
        
if round_number == 10:
    time.sleep(1)
    print()
    print("Game has ended")
        
        
print()
print()
        
#End game
time.sleep(2)
if computer1_score > computer2_score:
    print("Congratulations " + C1_name + ", for wining this game of scissors, paper , stone against " + C2_name)
    print()
    print("Final scores for " + C1_name + " and " + C2_name + ":")
    print(C1_name + ":" + str(computer1_score))
    print(C2_name + ":" + str(computer2_score))
elif computer2_score > computer1_score:
    print("Congratulations " + C2_name + ", for wining this game of scissors, paper , stone against " + C1_name)
    print()
    print("Final scores for " + C1_name + " and " + C2_name + ":")
    print(C1_name + ":" + str(computer1_score))
    print(C2_name + ":" + str(computer2_score))
elif computer1_score == computer2_score:
    print("Seems like is a tie... But is all right, next time, a champion shall prevail!")
    print()
    print("Final scores for " + C1_name + " and " + C2_name + ":")
    print(C1_name + ":" + str(computer1_score))
    print(C2_name + ":" + str(computer2_score))
else:
    print("ERROR : statement else printed.")
    print("Seems like there is a problem if you received this message, please inform Joon Hao know about this bug:(")

    
print()
print()

#outro
time.sleep(5)
print("Thank you for running this set of code and playing this game. Created by Joon Hao with Python 3.")




#Created by Joon Hao. Learned coding at sgcodecampus! 