#conversion caluclator by Joon Hao, build in Visual Studio Code, with Python 3

#import
import time, math

#variable
conversion = True

print("Welcome to conversion calculator")
print()
time.sleep(1.5)
#conversion
while conversion:
    user_convert = input("Which conversion would you like? ('quit' to quit programme)\n1. km -> m \n2. m -> cm \n3. km -> cm \n4. kilowatt/hr -> watt/hr \n5. tonnes -> kg \n6. miles -> km \n7. fahrenheit -> celsius \n")
    if user_convert == '1':
        print()
        #km -> m
        def convertkmtom(km):
            m = int(km) * 1000
            print(km + "km" + " = " + str(m) + "m")
        convertkmtom(input("Km: "))
        time.sleep(1.5)
        print()

    elif user_convert == '2':
        print()
        #m -> cm
        def convertmtocm(m):
            cm = int(m) * 100
            print(m + "m" + " = " + str(cm) + "cm") 
        convertmtocm(input("M: "))
        time.sleep(1.5)
        print()

    elif user_convert == '3':
        print()
        #km -> cm
        def convertkmtocm(km):
            cm = int(km) * 100000
            print(km + "km" + " = " + str(cm) + "cm") 
        convertkmtocm(input("Km: "))
        time.sleep(1.5)
        print()

    elif user_convert == '4':
        print()
        #kilowatt hr -> Watt hr
        def convertkwhtowh(kwh):
            wh = int(kwh) * 1000
            print(kwh + "kwh" + " = " + str(wh) + "Watts/hr") 
        convertkwhtowh(input("Kwh: "))
        time.sleep(1.5)
        print()

    elif user_convert == '5':
        print()
        #tonnes -> kg
        def converttonnestokg(tonnes):
            kg = int(tonnes) * 1000
            print(tonnes + "tonnes" + " = " + str(kg) + "kg") 
        converttonnestokg(input("tonnes: "))
        time.sleep(1.5)
        print()

    elif user_convert == '6':
        print()
        #mile -> km
        def convertmiletokm(mile):
            km = int(mile) * 1.609
            print(mile + "miles" + " = " + str(km) + "km") 
        convertmiletokm(input("miles: "))
        time.sleep(1.5)
        print()

    elif user_convert == '7':
        print()
        #fahrenheit -> celsius
        def convertftoc(f):
            c = (int(f) - 32) * 5/9
            c = round(c, 1)
            print(f + "°F" + " = " + str(c) + "°C") 
        convertftoc(input("Fahrenheit: "))
        time.sleep(1.5)
        print()

    elif user_convert == 'quit' or user_convert == "Quit":
        print()
        print()
        print("Programme shutting...")
        time.sleep(2)
        print()
        print("Bye bye")
        print()
        print("Build by Joon Hao, in Visual Studio Code with Python 3")
        conversion == False
        break

    else:
        print()
        print("Sorry, i didn't get that, please type out the number associated with the conversion you want or type 'quit' to exit.")
        time.sleep(1.5)
        print()