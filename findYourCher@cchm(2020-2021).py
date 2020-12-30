#findYourCher@cchm by bjh-developer, built in Visual Studio Code, with Python 3

#modules
from typing import AnyStr
import time

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
    names = ['Maglina Bte Ismail', 'Nurashikin Bte Mohamed Said', 'Loh Lai Yeow Daniel', 'Mohamed Almie Bin Mohamed Mazlan', 'Seng Mun Kong', 'Fu Chunyu Esther', 'Teo Lian Kiat', 'Hoe Ju Jin Junie', 'Lin Qinrong Michelle', 'Radiana Raza Ali', 'Siti Sarah Binte Mamat', 'Wong Ching-Yi Chesed', 'Wong Jing Xian Adeline', 'S N Muraledharan Naidu', 'Ho Si Ye Tammie', 'Khoo Sin Min Ambert', 'Rossenah Bte Kamis', 'Chen Jianwei Michael', 'Jonathan Yap Boon Kwang', 'Edmund Oh', 'Mohamed Ibrahim Bin Aris', 'Ong Lai Wei', 'Kee Chwee Hoon', 'Ong Siew Kim', 'Phang Yuh Koon', 'Shang Nannan', 'Wang Feng', 'Chan Xin Min', 'Chang Qi Yin Zoe Ruth', 'Chen Minhua', 'Tan Yen Lin', 'Qi Yan Ping', 'Fan Lijun', 'Om Wen Jie', 'Teo Yao Lu', 'Wang Wen', 'Wang Xiao', 'Wong Peng Kwee', 'Wu I-Husan', 'Yao Yadang', 'Azmi Bin Abdul Wahid', 'See Sze Ping', 'Yee Ren Ping Robbie', 'Ahmad Hashikin M B Mohd Latiff', 'Tang Xiu Hua Stefanie Michaela', 'Norashikin Bte Mohamed', 'Nurdiyana Binte Hamzah Lee', 'Surayah Bte Mohamed Anwar', 'Angela Yap', 'Fiona Chee Liee Horng', 'Ponni D/O Agoram', 'Sarah Ng Y L', 'Diana Angullia', 'Soh Guat Ee', 'Loh Siew Hua', 'Yeoh Zheng Sheng Alexandre Paul', 'Roziah Bte Ismail', 'Long Lay Na', 'Chua Chor Loon', 'Lim Wen Xi Alvin', 'Charmaine Loo', 'Joanna Tan', 'Veronica Tan', 'Claudia Chew Han Ngee ', 'Han Huayi', 'Tze Hui Yi', 'Khairunnisa Bte Yahya', 'Koh Rui Ling', 'Lai Han Wei', 'Shobitha D/O Vasudevan', 'Christin Pang', 'Kek Yee Ann', 'Quek Beng Hong', 'Toh Lay Hoon', 'Muhammad Vub Ismail', 'Ng See Khee Valerie', 'Lim Lymin Joel', 'Lin Guojing', 'Tan Han Kiang', 'Wu Derui', 'Lee Shu Ling Charlene Judith', 'Yee Kok Kheong ', 'Tan Pei Lee Jasmine', 'Peggy Yap', 'Michelle Foo', 'Char Wai Han Cassandra', 'Lim Chow Syan ', 'Tan Sek Jiau', 'Teo Tan Li Jaclyn', 'Yong Kian Yi Rachel', 'Michelle Chew', 'Chia Chooong Kwok Kelvin', 'Adlin Bte Idris', 'Alvin Ang Ban Leong', 'Ang Joo Seng Jason', 'Foo Kok Wei', 'Gan Choo Ming Lawrence', 'Jalaluddin Bin Hezan', 'Lam Tse Sun Samson', 'Ng Sin Wee Benny', 'Tay Han Seng Clement', 'Chow Yee Teng', 'Elizabeth So', 'Jasmine Fok', 'Tan Jo-Hsuan', 'Anisa Bte Mohamad Ali', 'Ong Shiau Chuen', 'Ho Yihan', 'Jun Liyana Binte Amin', 'Ong Xin Hui', 'Tan Seow Lan', 'Tay Hui Min']

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
    if user_input_init in updated_cher_names:
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