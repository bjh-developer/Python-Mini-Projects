#'Finding Pi with circle' by Joon Hao, built in Visual Studio Code, with Python 3

#import
import random, math

times = input("How many times you want to plot points for circle? ")
SquareArea = 0
CircleArea = 0

#plot points on a graph of a square containing a circle of radius 1
def plotPoints():
    global SquareArea, CircleArea, pie
    for i in range(int(times)):
        Xcor = random.uniform(0, 1)
        Ycor = random.uniform(0, 1)
        Dist = math.sqrt(Xcor**2 + Ycor**2)
        if Dist > 1:
            SquareArea += 1
        else:
            CircleArea += 1
            SquareArea += 1

#calculates the estimated value of pi
def CalcPi():
    global SquareArea, CircleArea, pie
    pie = (4 * (CircleArea/SquareArea))

#call out functions
plotPoints()
CalcPi()

#print out final statements
print(f'Number of points plotted within circle of radius of 1 = {CircleArea} \nNumber of total points plotted in the square containing circle radius of 1 = {SquareArea} \nPi equals to (estimated) = 4 * {CircleArea} / {SquareArea} = {pie}')