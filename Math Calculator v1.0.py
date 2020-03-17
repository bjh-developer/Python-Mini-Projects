#Math calculator v1.0 by Joon Hao, built in Visual Studio code, with Python 3

import time, math


#intro
print("Math calculator v1.0")
print("Made by Joon Hao")
print()
print()
print()
time.sleep(2)


#calculator
while True:
   user_menu = input("Open menu? ")
   if user_menu == "yes" or user_menu == "Yes":
      print("Options:")
      print()
      print("Enter 'add' or '1' to add two numbers")
      print()
      print("Enter 'subtract' or '2' to subtract two numbers")
      print()
      print("Enter 'multiply' or '3' to multiply two numbers")
      print()
      print("Enter 'divide' or '4' to divide two numbers")
      print()
      print("Enter 'area of square' or '5' to fine area of square")
      print()
      print("Enter 'area of rectangle' or '6' to find area of rectangle")
      print()
      print("Enter 'area of triangle' or '7' to find area of triangle")
      print()
      print("Enter 'area of parallelogram' or '8' to find area of parallelogram")
      print()
      print("Enter 'area of trapezium' or '9' to find area of trapezium")
      print()
      print("Enter 'volume of cube' or '10' to find volume of cube")
      print()
      print("Enter 'volume of cuboid' or '11' to find volume of cuboid")
      print()
      print("Enter 'volume of prism' or '12' to fine volume of prism")
      print()
      print("Enter 'volume of closed cylinder' or '13' to find volume of closed cylinder")
      print()
      print("Enter 'area of circle' or '14' to find the area of a circle")
      print()
      print("Enter 'circumference of circle' or '15' to find the area of a circle")
      print()
      print("Enter 'quadratic equation' or '16' to find the solutions")
      print()
      print("Enter 'quit' to end the program")
      user_input = input(": ")

      if user_input == "quit" or user_input == "Quit":
         print()
         print()
         print("Closing Math Calculator...")
         print("Made by Joon Hao")
         break     

      elif user_input == "add" or user_input == "Add" or user_input == "+" or user_input == "1":
         num1 = (input("Enter a number: "))
         num2 = (input("Enter a number: "))
         result = (int(num1) + int(num2))
         print()
         print(str(num1) + " + " + str(num2) + " = " + str(result))
         print("The answer is " + str(result))
         print()

      elif user_input == "subtract" or user_input == "Subtract" or user_input == "-" or user_input == "2":
         num1 = float(input("Enter a number: "))
         num2 = float(input("Enter a number: "))
         result = (num1 - num2)
         print()
         print(str(num1) + " - " + str(num2) + " = " + str(result))
         print("The answer is " + str(result))
         print()

      elif user_input == "multiply" or user_input == "Multiply" or user_input == "x" or user_input == "*" or user_input == "3":
         num1 = (input("Enter a number: "))
         num2 = (input("Enter a number: "))
         result = (int(num1) * int(num2))
         print()
         print(str(num1) + " x " + str(num2) + " = " + str(result))
         print("The answer is " + str(result))
         print()

      elif user_input == "divide" or user_input == "Divide" or user_input == "/" or user_input == "%" or user_input == "4":
         num1 = (input("Enter a number: "))
         num2 = (input("Enter a number: "))
         result = (int(num1) / int(num2))
         print()
         print(str(num1) + " / " + str(num2) + " = " + str(result))
         print("The answer is " + str(result))
         print()

      elif user_input == "area of square" or user_input == "Area of square" or user_input == "5":
         length = input("Length: ")
         breadth = input("Breadth: ")
         result = int(length) * int(breadth)
         print()
         print(str(length) + " x " + str(breadth) + " = " + str(result))
         print("Area of square is " + str(result))
         print()

      elif user_input == "area of rectangle" or user_input == "Area of rectangle" or user_input == "6":
         length = input("Length: ")
         breadth = input("Breadth: ")
         result = int(length) * int(breadth)
         print()
         print(str(length) + " x " + str(breadth) + " = " + str(result))
         print("Area of rectangle is " + str(result))
         print()

      elif user_input == "area of triangle" or user_input == "Area of triangle" or user_input == "7":
         breadth = input("Breadth: ")
         height = input("Height: ")
         result = 0.5 * int(breadth) * int(height)
         print()
         print("0.5" + " x " + str(breadth) + " x " + str(height))
         print("The area of triangle is " + str(result))
         print()

      elif user_input == "area of parallelogram" or user_input == "Area of parallelogram" or user_input == "8":
         breadth = input("Breadth: ")
         height = input("Height: ")
         result = int(breadth) * int(height)
         print()
         print(str(breadth) + " x " + str(height))
         print("The area of parallelogram is " + str(result))
         print()

      elif user_input == "area of trapezium" or user_input == "Area of trapezium" or user_input == "9":
         length_a = input("Length a: ")
         length_b = input("Length b: ")
         height = input("Height: ")
         result = 0.5 * (int(length_a) + int(length_b)) * int(height)
         print()
         print("0.5" + " x " + "(" + str(length_a) + " + " + str(length_b) + ")" + " x " + str(height))
         print("The area of trapezium is " + str(result))
         print()

      elif user_input == "area of circle" or user_input == "Area of circle" or user_input == "10":
         pie = 3.14
         num1 = (input("Enter the radius: "))
         result = (pie * int(num1)**2)
         print()
         print(str(pie) + " x " + str(num1) + "^2" + " = " + str(result))
         print("The area of the circle is " + str(result))
         print()

      elif user_input == "circumference of circle" or user_input == "Circumference of circle" or user_input == "11":
         pie = 3.14
         num1 = (input("Enter the radius: "))
         result = (2 * pie * int(num1))
         print()
         print("2 " + " x " + str(pie) + " x " + str(num1) + " = " + str(result))
         print("The circumference of the circle is " + str(result))
         print()

      elif user_input == "volume of cube" or user_input == "Volume of cube" or user_input == "12":
         length = input("Length: ")
         breadth = input("Breadth: ")
         height = input("Height: ")
         result = (int(length) * int(breadth) * int(height))
         print()
         print(length + " x " + breadth + " x " + height + " = " + str(result))
         print("The volume of cube is " + str(result))
         print()
         
      elif user_input == "volume of cuboid" or user_input == "Volume of cuboid" or user_input == "13":
         length = input("Length: ")
         breadth = input("Breadth: ")
         height = input("Height: ")
         result = int(length) * int(breadth) * int(height)
         print()
         print(str(length) + " x " + str(breadth) + " x " + str(height) + " = " + str(result))
         print("The volume of cuboid is " + str(result))
         print()

      elif user_input == "volume of prism" or user_input == "Volume of prism" or user_input == "14":
         area_of_cross_sect = input("Area of cross section: ")
         height = input("Height: ")
         result = int(area_of_cross_sect) * int(height)
         print()
         print(str(area_of_cross_sect) + " x " + str(height) + " = " + str(result))
         print("The volume of prism is " + str(result))
         print()

      elif user_input == "volume of closed cylinder" or user_input == "Volume of closed cylinder" or user_input == "15":
         pie = 3.14
         radius = input("Radius: ")
         height = input("Height: ")
         result = int(pie) * int(radius)^2 * int(height)
         print()
         print(str(pie) + " x " + str(radius) + "^2" + " x " + str(height) + " = " + str(result))
         print("The volume of closed cylinder is " + str(result))
         print()

      elif user_input == "quadratic equation" or user_input == "Quadratic equation" or user_input == "ax^2 + bx + c = 0" or user_input == "16":
         user_input_a = input("a: ")
         user_input_b = input("b: ")
         user_input_c = input("c: ")
         d = (int(user_input_b)**2) - (4 * int(user_input_a) * int(user_input_c))
         sol1 = (-int(user_input_b) - math.sqrt(d))/(2 * int(user_input_a))
         sol2 = (-int(user_input_b) + math.sqrt(d))/(2 * int(user_input_a))
         print()
         print(str(user_input_a) + "x^2" + " + " + str(user_input_b) + "x" + " + " + str(user_input_c) + " = " + str(sol1) + " or " + str(sol2))
         print('The solution are {0} or {1}'.format(sol1,sol2))
         print()

      else:
         print("Unknown input, please try again")

   elif user_menu == "no" or user_menu == "No":
      break

   else:
      print("Unknown input, please try again")