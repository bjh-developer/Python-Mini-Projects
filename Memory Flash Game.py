#Let's make a game!
#The game plays like this: Each level, a series of numbers (0 to 9) will be flashed, and each number is flashed 
#at a regular interval (like blinking - show 1 number, clear it, show 2nd number, etc). 
#So level 1 has 1 number, level 2 has 2 and so on. When the entire series is shown
#we ask the player to answer, what were the numbers he/she saw. E.g. if he saw 1, 2, 3, his answer should be '123'.
#If he answers correctly, he goes on to the next level. If not, it's game over!
#To start the game, we can print 'Ready?' and wait for 1 second, and start flashing.

#We shall learn to organise our game and divide it up into specific tasks. And what is a block of code that does a
#specific task?
#Tasks:
#1. Start/Manage the game - start the game, and generally run the game
#2. Generate the series of numbers
#3. Flash the numbers
#4. Get the answer from the player
#5. Check the answer against the series (optional, we can put this in 1.)

import time
import random
import os

game = True
round = 1
comp_num = []
check_num = ''
user_ans = ''

def generate_series():
    # Generates the number series for the round
    for i in range(round):
        global comp_num
        comp_num.append(random.randint(0, 9))

def start_round():
    # Flashes the numbers and asks the user for the answer
    os.system('clear')
    for j in range(len(comp_num)):
        print(comp_num[j])
        time.sleep(0.5)
        os.system('clear')
        print()
        time.sleep(0.2)
        os.system('clear')
    global user_ans
    user_ans = input("What is your answer? ")
    
def get_answer():
    #Request answer from player
    global comp_num
    global check_num
    global user_ans
    check_num = ''.join(str(v) for v in comp_num)
    
def start_game():
    #Initialises the game and starts the first round
    global user_ready, game
    print('Welcome to the Memory Flash Game!')
    time.sleep(1.5)
    print()
    print('Instructions:\n1. Numbers will start appearing on your screen and you must remember them.\n2. You will have to type out the numbers you memorised and if you got it right, you move on to the next level, if not byebye.')
    time.sleep(3)
    print()
    user_ready = input('Are you ready [Y/N]?')

    if user_ready == 'Y' or user_ready == 'y':
        print()
        print("EYES ON THE SCREEN")
        print()
        time.sleep(2)
        game = True

    elif user_ready == 'N' or user_ready == 'n':
        print('Alright, you can come back anytime!')
        print()
        time.sleep(2)
        print('byebye!')
        game = False

    else:
        print('Sorry, please enter Y/N')
        start_game()

    time.sleep(1)
    #os.system('clear')

#callout
start_game()
while game:

    generate_series()
    start_round()
    get_answer()

    if user_ans != check_num:
        print('Oh man... you loss.')
        print()
        time.sleep(2)
        print('You can re-try the game next time, just re-run the code :)')
        print()
        time.sleep(2)
        print('Byebye!')
        print()
        print()
        print('Memory Flash Game by bjh-developer, built in Visual Studio Code, with Python 3')
        game = False
        
    elif user_ans == check_num:
        round += 1
        comp_num.clear()
        print(f'Congratulations! You win! Time to go on to the next level! (Round number = number of digits: {round})')
        print()
        time.sleep(3.5)
        print("EYES ON THE SCREEN")
        time.sleep(2)
    else:
        print('error1')