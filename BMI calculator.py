#BMI calculator created by Joon Hao, built in Visual Studio Code with Python 3

import time


#person's info
user_name = input("What is your name: ")
user_weight = input("What is your weight(KG): ")
user_height = input("What is your height(metre): ")

#calculator
def bmi_calculator(name, weight, height):
    bmi = weight / (height ** 2)
    print("BMI: ")
    print(bmi)
    if bmi >= 18.5 and bmi < 23:
        return name + " BMI is normal!"
    elif bmi < 18.5:
        return name + " at low risk but increased risk of nutritional deficiency and osteoporosis!"
    else:
        return name + " is at high risk!"

result_1 = bmi_calculator(user_name, float(user_weight), float(user_height))
print(str(result_1))