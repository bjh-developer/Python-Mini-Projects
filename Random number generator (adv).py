#imports the module 'random' & 'time'
import random, time

#declaring variables
sessions = 0
numListPrinted = []
archive = []
archive_times = 0

#ask user what is the number range for random number generator
lowerLimit = int(input('What is the lowest number you want in your random: '))
upperLimit = int(input('What is the highest number you want in your random: '))
user_replacement = int(input('How many times before number can be reused (if don\'t want any repeating, type in 0): '))
total = upperLimit - (lowerLimit - 1)

print('\n--------------------------------------------------------\n')

#defines function to generate random number
def generate_num():

    #starts the timer to time the duration taken to generate numbers
    start = time.process_time()
    
    while True:
        global sessions, archive_times

        #ask user how many random numbers he wants to generate
        times = int(input('How many numbers: '))
        
        #while loop to generate user_number of random numbers
        while times > 0:
            times -= 1
            number = random.randint(lowerLimit, upperLimit)

            #checks if the number has been generated in previous generations
            if number not in archive:
                numListPrinted.append(number)
                archive.append(number)
                archive_times += 1
                if user_replacement == 0:
                    pass
                else:
                    if archive_times > user_replacement:
                        archive.pop(0)
                    else:
                        pass
            else:
                #extra layer of checking to check if all numbers has been exhausted
                if len(archive) == total:
                    print('All numbers have been exhausted since non-repeating including past generations.\nBye bye!')
                    #programme quits when all possible numbers in user_range has been generated
                    exit()
                else:
                    times += 1
    
        #printing of results
        sessions += 1
        print(f'\nYour randomly generated numbers are: {numListPrinted}')
        print(f'Generation number = {sessions}')
        print(f'Time taken for generation = {time.process_time() - start} seconds')

        #if else statement to check if user wants to generate again
        cont = input('Do you wish to generate another series of numbers [y/n]: ')
        if cont.lower() == 'n':
            print("\nBye bye")
            break
        elif cont.lower() == 'y':
            numListPrinted.clear()
            print('\n--------------------------------------------------------\n')
        else:
            print('\nError, please key in y or n, please re-run code')
            break

#calling function
generate_num()
