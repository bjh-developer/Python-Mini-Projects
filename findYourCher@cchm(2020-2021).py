#findYourCher@cchm by bjh-developer, built in Visual Studio Code, with Python 3

#modules
from typing import AnyStr
import time, random

#get the initial of the teacher's name
def get_initials(fullname):
    xs = (fullname)
    name_list = xs.split()
    initials = ""

    for name in name_list:  # go through each name  
        initials += name[0].upper()  # append the initial

    return initials

#pairs up the teacher's name with his/her initials in dictionary
def process():
    global answer, chosen_name, updated_cher_names
    answer = ''
    chosen_name = ''
    cher_names = {answer: chosen_name}
    count = 0
    names = ['Maglina Bte Ismail', 'Nurashikin Bte Mohamed Said', 'Loh Lai Yeow Daniel', 'Mohamed Almie Bin Mohamed Mazlan', 'Seng Mun Kong', 'Fu Chunyu Esther', 'Teo Lian Kiat', 'Hoe Ju Jin Junie', 'Lin Qinrong Michelle', 'Radiana Raza Ali', 'Siti Sarah Binte Mamat', 'Wong Ching-Yi Chesed', 'Wong Jing Xian Adeline', 'S N Muraledharan Naidu', 'Ho Si Ye Tammie', 'Khoo Sin Min Ambert', 'Rossenah Bte Kamis', 'Chen Jianwei Michael', 'Jonathan Yap Boon Kwang', 'Edmund Oh', 'Mohamed Ibrahim Bin Aris', 'Ong Lai Wei', 'Kee Chwee Hoon', 'Ong Siew Kim', 'Phang Yuh Koon', 'Shang Nan Nan', 'Wang Y Feng', 'Chan Xin Min', 'Chang Qi Yin Zoe Ruth', 'Chen Minhua', 'Tan Yen Lin', 'Qi Yan Ping', 'Fan Lijun', 'Om Wen Jie', 'Teo Yao Lu', 'Wang Wen', 'Wang Xiao', 'Wong Peng Kwee', 'Wu I-Husan', 'Yao Yadang', 'Azmi Bin Abdul Wahid', 'See Sze Ping', 'Yee Ren Ping Robbie', 'Ahmad Hashikin M B Mohd Latiff', 'Tang Xiu Hua Stefanie Michaela', 'Norashikin Bte Mohamed', 'Nurdiyana Binte Hamzah Lee', 'Surayah Bte Mohamed Anwar', 'Angela Yap', 'Fiona Chee Liee Horng', 'Ponni D/O Agoram', 'Sarah Ng Y L', 'Diana Angullia', 'Soh Guat Ee', 'Loh Siew Hua', 'Yeoh Zheng Sheng Alexandre Paul', 'Roziah Bte Ismail', 'Long Lay Na', 'Chua Chor Loon', 'Lim Wen Xi Alvin', 'Charmaine Loo', 'Joanna Tan', 'Veronica Tan', 'Claudia Chew Han Ngee ', 'Han Huayi', 'Tze Hui Yi', 'Khairunnisa Bte Yahya', 'Koh Rui Ling', 'Lai Han Wei', 'Shobitha D/O Vasudevan', 'Christin Pang', 'Kek Yee Ann', 'Quek Beng Hong', 'Toh Lay Hoon', 'Muhammad Vub Ismail', 'Ng See Khee Valerie', 'Lim Lymin Joel', 'Lin Guojing', 'Tan Han Kiang', 'Wu Derui', 'Lee Shu Ling Charlene Judith', 'Yee Kok Kheong ', 'Tan Pei Lee Jasmine', 'Peggy Yap', 'Michelle Foo', 'Char Wai Han Cassandra', 'Lim Chow Syan ', 'Tan Sek Jiau', 'Teo Tan Li Jaclyn', 'Yong Kian Yi Rachel', 'Michelle Chew', 'Chia Chooong Kwok Kelvin', 'Adlin Bte Idris', 'Alvin Ang Ban Leong', 'Ang Joo Seng Jason', 'Foo Kok Wei', 'Gan Choo Ming Lawrence', 'Jalaluddin Bin Hezan', 'Lam Tse Sun Samson', 'Ng Sin Wee Benny', 'Tay Han Seng Clement', 'Chow Yee Teng', 'Elizabeth So', 'Jasmine Fok', 'Tan Jo-Hsuan', 'Anisa Bte Mohamad Ali', 'Ong Shiau Chuen', 'Ho Yihan', 'Jun Liyana Binte Amin', 'Ong Xin Hui', 'Tan Seow Lan', 'Tay Hui Min']

    for i in names:
        chosen_name = i
        answer = get_initials(i)
        count += 1

        if count == 1:
            updated_cher_names = {**cher_names, **{answer: chosen_name}}

        elif count > 1:
            updated_cher_names = {**updated_cher_names, **{answer: chosen_name}}
            
#calls out
process()

#ui
run = True
print("Hi, this programme has been made by Joon Hao for you to find your teacher full name!")
print('Note that this is updated on 30 dec 2020')
while run:
    global updated_cher_names
    time.sleep(2)
    print()
    user_input_init = input("Teacher's initial: ")
    user_input_subj = input("Subject: ")
    print()

    #checks for correct initials, if no, repeat with error message
    if user_input_init == '0':
      print("You lucky, you found the esater egg, but sadly there's nothing fun here, it is just for fun lol...")
      time.sleep(3)
      print()
      print()
      easter_game = input('But actually, there is a game, do you want to play it? (Y/N) ')
      if easter_game == 'Y' or easter_game == 'y':
        #variables
        game = True
        word = "Extravagant"
        round = 10


        while game:
            #intro
            print("Welcome to hangman v2.")
            time.sleep(1.5)
            print("Let's see if you can figure that lucky word.")
            print()
            print()
            time.sleep(2)


            #instructions
            print("Instructions for this game:\n1. You are to guess the word in 10 tries\n2. You are allowed to guess the letters of the lucky word 9 times.\n3. The last try, you would have to guess the word, if not, I (the host) win!")
            print()
            time.sleep(3.5)


            #Game starting
            print()
            print("Ready!")
            time.sleep(1)
            print("Set!")
            time.sleep(1)
            print("GO!")
            time.sleep(1)
            print()
            print()
            
            #game 
            print("The lucky word is a 11 letter word, adjective\nmeaning: lacking restraint in spending money or using resources.")
            word_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
            while round > 1:
                round = round - 1
                guess = input("guess: ")

                #analysis
                if guess == "e" or guess == "E":
                    word_game[0] = "E"
                    print(word_game)
                    print()

                elif guess == "x" or guess == "X":
                    word_game[1] = "x"
                    print(word_game)
                    print()

                elif guess == "t" or guess == "T":
                    word_game[2] = "t"
                    word_game[10] = "t"
                    print(word_game)
                    print()

                elif guess == "r" or guess == "R":
                    word_game[3] = "r"
                    print(word_game)
                    print()

                elif guess == "a" or guess == "A":
                    word_game[4] = "a"
                    word_game[6] = "a"
                    word_game[8] = "a"
                    print(word_game)
                    print()

                elif guess == "v" or guess == "V":
                    word_game[5] = "v"
                    print(word_game)
                    print()

                elif guess == "g" or guess == "G":
                    word_game[7] = "g"
                    print(word_game)
                    print()

                elif guess == "n" or guess == "N":
                    word_game[9] = "n"
                    print(word_game)
                    print()

                else:
                    print("Nope, there isn't a " + guess + " in the lucky word.")
                    time.sleep(2)
                    print()

                #attempts left str
                print("You left " + str(round) + " attempts!")

            
            #last round
            if round == 1:
                round = round - 1
                print("Last attempt, time to guess your word!")
                time.sleep(2)
                guess_word = input("What is the word?\n")

                #analysis
                if guess_word == "Extravagant" or guess_word == "extravagant":
                    print()
                    print("Once again you beat me. Congrates!")
                    time.sleep(3.5)

                else:
                    print()
                    print("Oops, seems like you guessed it wrong :(")
                    time.sleep(2.5)

                #user choice to restart
                user_restart = input("Do you want to play again? (y/n)\n")
                if user_restart == "y" or user_restart == "Y":
                    round = 10
                    print()
                    print('**************************************')
                    print()
                    game == True
                    
                
                elif user_restart == "n" or user_restart == "N":
                    print("Bye, bye.")
                    print()
                    print("Hangman v2 by Joon Hao, build in Visual Studio Code with Python 3.")
                    game == False
                    break

                else:
                    user_restart = input("Sorry, I didn't get you there. Please reply with y/n")

            else:
                pass

      elif easter_game == 'N' or easter_game == 'n':
        print('Fine, no games.')
      else:
        print('Sorry, please key in either Y (yes) or N (no)')  
            
    elif user_input_init in updated_cher_names:
        print(f'Your teacher for {user_input_subj} is {updated_cher_names[user_input_init]}')
    else:
        print("Sorry, we currently do not have that teacher's name in our database :(")

    time.sleep(2)
    user_input_run = input('Do you want to continue finding? (Y/N) ')
    if user_input_run == 'Y' or user_input_run == 'y':
        print()
        print()
        pass
    elif user_input_run == 'N' or user_input_run == 'n':
        print()
        print('Goodbye!')
        print('findYourCher@cchm by bjh-developer, built in Visual Studio Code, with Python 3')
        break
    else:
        print('Please key in Y (yes) or N (no)')
        print()