#Lucky number guessing game by Joon Hao. Built in Visual Studio Code IDE, with Python 3.

#import
import time


#Dev info
#Lucky number is "13"

#intro
print("Welcome to a game of Lucky Or Not?(aka Number guessing game)")
time.sleep(2)
print()
print()
print("I'm feeling lucky! (Totally not from Google)")
time.sleep(1.5)
print()
print()
print()

#Instructions
print("Instructions for this game:")
print()
print("1. You will be given 3 chances to guess my lucky number. If you managed to guess my lucky number within the 3 chances, you win.")
print("   If not, you loss :(")
print()
print()
time.sleep(4)
print("If not, let's get started!")
print()
print()
print()


#game starting or ending (based on user input)
user_lon = input("Are you feeling lucky today, now? ans(Yes / No)")
if user_lon == "yes" or user_lon == "Yes":
    print("Alright, get ready for your lucky game!")
    time.sleep(3)

    #game countdown
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

    #game starts
    print("Let's go! (Developer [Joon Hao]: Pst... Good luck because this game is just the first version, soooo I'm going to let it be easy but remember player...")
    time.sleep(6)
    print("This game is called 'Lucky Or Not' for a good reason")
    time.sleep(5)

    #round 1
    user_lucky_number = input("What will be my lucky number? (Hint: My lucky number is between 0 to 15) ")
    print("You chose " + user_lucky_number)
    time.sleep(1)
    print("But will it be my lucky number?")
    time.sleep(3)

    #Round 1 guess correct
    if user_lucky_number == "13":
        print("YES! Congratultions, you managed to guess my lucky number in 1 try!")
        time.sleep(2)
        print("Now that is what I call 'A LUCKY PERSON ON HIS/HER LUCKY DAY!'")
    
    #Round 1 guess wrong
    elif user_lucky_number != "13":
        print("Unfortunately, no. That is not my lucky number :(")
        time.sleep(2)
        print("But don't worry, you still have 2 more chances to guess my lucky number. (Hopefully by the next chance)")
        time.sleep(2)
        user_hint_1 = input("Do you want a hint? Ans(Yes / No)")



        #Round 2 yes hint
        if user_hint_1 == "Yes" or user_hint_1 == "yes":
            print("Hint: My lucky number is an odd number (That should helped you, I think...)")
            time.sleep(2)

            #Round 2
            user_lucky_number_2 = input("Sooooo, what's my lucky number?")
            print("You chose " + user_lucky_number_2)
            time.sleep(1)
            print("But will it be my lucky number?")
            time.sleep(3)

            #Round 2 guess correct
            if user_lucky_number_2 == "13":
                print("And the answer is YES!!! Congratulations! 2nd time is always the charm (maybe).")
                time.sleep(2)
                print("Now that is what I call 'A LUCKY PERSON ON HIS/HER '2nd' LUCKY DAY!'")

            #Round 2 guess wrong
            elif user_lucky_number_2 != "13":
                print("Unfortunately, no again. I'm so sorry, maybe today wasn't your lucky day... or is it (hmmmmm)")
                time.sleep(3)
                print("People always say '3rd time is the charm', maybe that will apply to you today???")
                time.sleep(2)
                print("Don't give up. You still have 1 more attempt, you can do it!")
                time.sleep(2)
                user_hint_2 = input("Do you want the final hint? Ans(Yes / No)")


                #Round 3 yes hint
                if user_hint_2 == "Yes" or user_hint_2 == "yes":
                    print("Last hint: my lucky number is more than 12 (Now that is what I call a big hint)")
                    time.sleep(2)

                    #Round 3
                    user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")
                    
                    #Round 3 guess correct
                    if user_lucky_number_3 == "13":
                        print("Since is your last chance and you might be nervous, I will cut to the chase")
                        time.sleep(1)
                        print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                    #Round 3 wrong guess
                    elif user_lucky_number_3 != "13":
                        print(":|")
                        time.sleep(0.7)
                        print("I am so sorry but no.")
                        time.sleep(1.2)
                        print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")

                    #Round 3 2nd ERROR message
                    else:
                        print(":(")
                        print("ERROR : BUG DETECTED! CODELINE : 138")
                        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                #Round 3 no hint
                elif user_hint_2 == "No" or user_hint_2 == "no":
                    print("You sure? Remember, this is your last chance. But even if you regret now, there is no turning back like in life...")
                    time.sleep(2)
                    #Round 3
                    user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")

                    #Round 3 guess correct
                    if user_lucky_number_3 == "13":
                        print("Since is your last chance and you might be nervous, I will cut to the chase")
                        time.sleep(1)
                        print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                    #Round 3 wrong guess
                    elif user_lucky_number_3 != "13":
                        print(":|")
                        time.sleep(0.7)
                        print("I am so sorry but no.")
                        time.sleep(1.2)
                        print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")
                        #Round 3 2nd ERROR message
                    else:
                        print(":(")
                        print("ERROR : BUG DETECTED! CODELINE : 164")
                        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                #Round 3 ERROR message
                else:
                    print(":(")
                    print("ERROR : BUG DETECTED! CODELINE : 170")
                    print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

            #Round 2 ERROR message
            else:
                print(":(")
                print("ERROR : BUG DETECTED! CODELINE : 176")
                print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

        
        #Round 2 no hint
        elif user_hint_1 == "No" or user_hint_1 == "no":
            print("That might be a bad choice but ok. Wish granted...")
            time.sleep(2)

            #Round 2
            user_lucky_number_2 = input("Sooooo, what's my lucky number?")
            print("You chose " + user_lucky_number)
            time.sleep(1)
            print("But will it be my lucky number?")
            time.sleep(3)

            #Round 2 guess correct
            if user_lucky_number_2 == "13":
                print("And the answer is YES!!! Congratulations! 2nd time is always the charm (maybe).")
                time.sleep(2)
                print("Now that is what I call 'A LUCKY PERSON ON HIS/HER '2nd' LUCKY DAY!'")

            #Round 2 guess wrong
            elif user_lucky_number_2 != "13":
                print("Unfortunately, no again. I'm so sorry, maybe today wasn't your lucky day... or is it (hmmmmm)")
                time.sleep(3)
                print("People always say '3rd time is the charm', maybe that will apply to you today???")
                time.sleep(2)
                print("Don't give up. You still have 1 more attempt, you can do it!")
                time.sleep(2)
                user_hint_2 = input("Do you want the final hint? Ans(Yes / No)")


                #Round 3 yes hint
                if user_hint_2 == "Yes" or user_hint_2 == "yes":
                    print("Last hint: my lucky number is more than 12 (Now that is what I call a big hint)")
                    time.sleep(2)

                    #Round 3
                    user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")
                    
                    #Round 3 guess correct
                    if user_lucky_number_3 == "13":
                        print("Since is your last chance and you might be nervous, I will cut to the chase")
                        time.sleep(1)
                        print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                    #Round 3 wrong guess
                    elif user_lucky_number_3 != "13":
                        print(":|")
                        time.sleep(0.7)
                        print("I am so sorry but no.")
                        time.sleep(1.2)
                        print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")

                    #Round 3 2nd ERROR message
                    else:
                        print(":(")
                        print("ERROR : BUG DETECTED! CODELINE : 234")
                        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                #Round 3 no hint
                elif user_hint_2 == "No" or user_hint_2 == "no":
                    print("You sure? Remember, this is your last chance. But even if you regret now, there is no turning back like in life...")
                    time.sleep(2)
                    #Round 3
                    user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")

                    #Round 3 guess correct
                    if user_lucky_number_3 == "13":
                        print("Since is your last chance and you might be nervous, I will cut to the chase")
                        time.sleep(1)
                        print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                    #Round 3 wrong guess
                    elif user_lucky_number_3 != "13":
                        print(":|")
                        time.sleep(0.7)
                        print("I am so sorry but no.")
                        time.sleep(1.2)
                        print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")
                        #Round 3 2nd ERROR message
                    else:
                        print(":(")
                        print("ERROR : BUG DETECTED! CODELINE : 260")
                        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                #Round 3 ERROR message
                else:
                    print(":(")
                    print("ERROR : BUG DETECTED! CODELINE : 266")
                    print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")


            #Round 2 ERROR message
            else:
                print(":(")
                print("ERROR : BUG DETECTED! CODELINE : 273")
                print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

        #Round 2 ERROR message
        else:
            print(":(")
            print("ERROR : BUG DETECTED! CODELINE : 279")
            print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")


    #Round 1 ERROR message
    else:
        print(":(")
        print("ERROR : BUG DETECTED! CODELINE : 286")
        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")                  



#User chose not lucky
elif user_lon == "no" or user_lon == "No":
    user_no_next = input("Is alright, you can wait for your lucky day again then play this game or play now and see how unlucky your day is? (Ans: Wait / Play)")

    #Second consideration to play or not
    #Don't to play
    if user_no_next == "Wait" or user_no_next == "wait":
        print("Ok, no problem. I am not going to force you to play since you are already feeling unlucky...")
        time.sleep(2)
        print("If you had played this game, I can 100 percent guarantee you will feel so unlucky that you develop depression (which I don't wish any players will)")
    
    #Want to play
    elif user_no_next == "Play" or user_no_next == "play":
        print("You sure about this??? Ok fine, I will let you play. (The developer 'Joon Hao' will not be responsible for any player who suffers depression after this warning and game, TOTALLY NOT RESPONSIBLE FOR IT)")
        time.sleep(6)
        #game countdown
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

        #game starts
        print("Let's go! (Developer ([Joon Hao]): Pst... Good luck because this game is just the first version, soooo I'm going to let it be easy but remember player...")
        time.sleep(6)
        print("This game is called 'Lucky Or Not' for a good reason")
        time.sleep(5)

        #round 1
        user_lucky_number = input("What will be my lucky number? (Hint: My lucky number is between 0 to 15) ")
        print("You chose " + user_lucky_number)
        time.sleep(1)
        print("But will it be my lucky number?")
        time.sleep(3)

        #Round 1 guess correct
        if user_lucky_number == "13":
            print("YES! Congratultions, you managed to guess my lucky number in 1 try!")
            time.sleep(2)
            print("Now that is what I call 'A LUCKY PERSON ON HIS/HER LUCKY DAY!'")
        
        #Round 1 guess wrong
        elif user_lucky_number != "13":
            print("Unfortunately, no. That is not my lucky number :(")
            time.sleep(2)
            print("But don't worry, you still have 2 more chances to guess my lucky number. (Hopefully by the next chance)")
            time.sleep(2)
            user_hint_1 = input("Do you want a hint? Ans(Yes / No)")



            #Round 2 yes hint
            if user_hint_1 == "Yes" or user_hint_1 == "yes":
                print("Hint: My lucky number is an odd number (That should helped you, I think...)")
                time.sleep(2)

                #Round 2
                user_lucky_number_2 = input("Sooooo, what's my lucky number?")
                print("You chose " + user_lucky_number_2)
                time.sleep(1)
                print("But will it be my lucky number?")
                time.sleep(3)

                #Round 2 guess correct
                if user_lucky_number_2 == "13":
                    print("And the answer is YES!!! Congratulations! 2nd time is always the charm (maybe).")
                    time.sleep(2)
                    print("Now that is what I call 'A LUCKY PERSON ON HIS/HER '2nd' LUCKY DAY!'")

                #Round 2 guess wrong
                elif user_lucky_number_2 != "13":
                    print("Unfortunately, no again. I'm so sorry, maybe today wasn't your lucky day... or is it (hmmmmm)")
                    time.sleep(3)
                    print("People always say '3rd time is the charm', maybe that will apply to you today???")
                    time.sleep(2)
                    print("Don't give up. You still have 1 more attempt, you can do it!")
                    time.sleep(2)
                    user_hint_2 = input("Do you want the final hint? Ans(Yes / No)")


                    #Round 3 yes hint
                    if user_hint_2 == "Yes" or user_hint_2 == "yes":
                        print("Last hint: my lucky number is more than 12 (Now that is what I call a big hint)")
                        time.sleep(2)

                        #Round 3
                        user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")
                        
                        #Round 3 guess correct
                        if user_lucky_number_3 == "13":
                            print("Since is your last chance and you might be nervous, I will cut to the chase")
                            time.sleep(1)
                            print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                        #Round 3 wrong guess
                        elif user_lucky_number_3 != "13":
                            print(":|")
                            time.sleep(0.7)
                            print("I am so sorry but no.")
                            time.sleep(1.2)
                            print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")

                        #Round 3 2nd ERROR message
                        else:
                            print(":(")
                            print("ERROR : BUG DETECTED! CODELINE : 403")
                            print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                    #Round 3 no hint
                    elif user_hint_2 == "No" or user_hint_2 == "no":
                        print("You sure? Remember, this is your last chance. But even if you regret now, there is no turning back like in life...")
                        time.sleep(2)
                        #Round 3
                        user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")

                        #Round 3 guess correct
                        if user_lucky_number_3 == "13":
                            print("Since is your last chance and you might be nervous, I will cut to the chase")
                            time.sleep(1)
                            print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                        #Round 3 wrong guess
                        elif user_lucky_number_3 != "13":
                            print(":|")
                            time.sleep(0.7)
                            print("I am so sorry but no.")
                            time.sleep(1.2)
                            print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")
                            #Round 3 2nd ERROR message
                        else:
                            print(":(")
                            print("ERROR : BUG DETECTED! CODELINE : 429")
                            print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                    #Round 3 ERROR message
                    else:
                        print(":(")
                        print("ERROR : BUG DETECTED! CODELINE : 435")
                        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                #Round 2 ERROR message
                else:
                    print(":(")
                    print("ERROR : BUG DETECTED! CODELINE : 441")
                    print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

            
            #Round 2 no hint
            elif user_hint_1 == "No" or user_hint_1 == "no":
                print("That might be a bad choice but ok. Wish granted...")
                time.sleep(2)

                #Round 2
                user_lucky_number_2 = input("Sooooo, what's my lucky number?")
                print("You chose " + user_lucky_number_2)
                time.sleep(1)
                print("But will it be my lucky number?")
                time.sleep(3)

                #Round 2 guess correct
                if user_lucky_number_2 == "13":
                    print("And the answer is YES!!! Congratulations! 2nd time is always the charm (maybe).")
                    time.sleep(2)
                    print("Now that is what I call 'A LUCKY PERSON ON HIS/HER '2nd' LUCKY DAY!'")

                #Round 2 guess wrong
                elif user_lucky_number_2 != "13":
                    print("Unfortunately, no again. I'm so sorry, maybe today wasn't your lucky day... or is it (hmmmmm)")
                    time.sleep(3)
                    print("People always say '3rd time is the charm', maybe that will apply to you today???")
                    time.sleep(2)
                    print("Don't give up. You still have 1 more attempt, you can do it!")
                    time.sleep(2)
                    user_hint_2 = input("Do you want the final hint? Ans(Yes / No)")


                    #Round 3 yes hint
                    if user_hint_2 == "Yes" or user_hint_2 == "yes":
                        print("Last hint: my lucky number is more than 12 (Now that is what I call a big hint)")
                        time.sleep(2)

                        #Round 3
                        user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")
                        
                        #Round 3 guess correct
                        if user_lucky_number_3 == "13":
                            print("Since is your last chance and you might be nervous, I will cut to the chase")
                            time.sleep(1)
                            print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                        #Round 3 wrong guess
                        elif user_lucky_number_3 != "13":
                            print(":|")
                            time.sleep(0.7)
                            print("I am so sorry but no.")
                            time.sleep(1.2)
                            print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")

                        #Round 3 2nd ERROR message
                        else:
                            print(":(")
                            print("ERROR : BUG DETECTED! CODELINE : 499")
                            print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                    #Round 3 no hint
                    elif user_hint_2 == "No" or user_hint_2 == "no":
                        print("You sure? Remember, this is your last chance. But even if you regret now, there is no turning back like in life...")
                        time.sleep(2)
                        #Round 3
                        user_lucky_number_3 = input("Sooooooo, for the final time. What is my lucky number?")

                        #Round 3 guess correct
                        if user_lucky_number_3 == "13":
                            print("Since is your last chance and you might be nervous, I will cut to the chase")
                            time.sleep(1)
                            print("And is n.. YES!!!! Congratulations, you are indeed the person who believes in '3rd time is a charm'")

                        #Round 3 wrong guess
                        elif user_lucky_number_3 != "13":
                            print(":|")
                            time.sleep(0.7)
                            print("I am so sorry but no.")
                            time.sleep(1.2)
                            print("Don't feel sad (although i know you won't...), you may not be lucky today, but you got even luckier days ahead to be happy and grateful about. ")
                            #Round 3 2nd ERROR message
                        else:
                            print(":(")
                            print("ERROR : BUG DETECTED! CODELINE : 525")
                            print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

                    #Round 3 ERROR message
                    else:
                        print(":(")
                        print("ERROR : BUG DETECTED! CODELINE : 531")
                        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")


                #Round 2 ERROR message
                else:
                    print(":(")
                    print("ERROR : BUG DETECTED! CODELINE : 538")
                    print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")

            #Round 2 ERROR message
            else:
                print(":(")
                print("ERROR : BUG DETECTED! CODELINE : 544")
                print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")


        #ERROR message
        else:
            print(":(")
            print("ERROR : BUG DETECTED! CODELINE : 551")
            print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")



                        

    #ERROR message
    else:
        print(":(")
        print("ERROR : BUG DETECTED! CODELINE : 561")
        print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ") 
        
#ERROR message
else:
    print(":(")
    print("ERROR : BUG DETECTED! CODELINE : 567")
    print(":/ OH NO, IF YOU SEE THIS MESSAGE, PLEASE INFORM JOON HAO ABOUT THIS PROBLEM :/ ")



#Outro
time.sleep(6)
print("Seems like you beat me this time round, but i will be back to take my revenge!")
time.sleep(5.5)
print("The End")
time.sleep(2.5)
print("Thank you for running this set of codes and playing this game.")
print("Created by Joon Hao, built in Visual Studio Code IDE, with Python 3")