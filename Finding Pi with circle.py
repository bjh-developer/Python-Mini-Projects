#'Finding Pi with circle' by Joon Hao, built in Visual Studio Code, with Python 3

#import
import random, math, time
import matplotlib.pyplot as plt
import numpy as np

times = input("How many times you want to plot points for circle? ")
SquareArea = 0
CircleArea = 0
AllPoints = []

#plot points on a graph of a square containing a circle of radius 1
def plotPoints():
    global SquareArea, CircleArea, pie, Xcor, Ycor, AllPoints, string
    for i in range(int(times)):
        Xcor = random.uniform(0, 1)
        Ycor = random.uniform(0, 1)
        string = str(Xcor) + "," + str(Ycor)
        AllPoints.append(string)
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


#visual representation
def plotGraph():
    global figure
    figure, axes = plt.subplots()
    Drawing_uncolored_circle = plt.Circle( (0.0, 0.0 ), 1.0 , fill = False )
    axes.set_aspect( 1 )
    axes.add_artist( Drawing_uncolored_circle )
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    x = [float(i.split(',')[0]) for i in AllPoints]
    y = [float(i.split(',')[1]) for i in AllPoints]
    plt.plot(x, y, 'o', markersize=2, markeredgecolor="red", markerfacecolor="red")
    plt.title(f'Num pts. in circle/total = {CircleArea}/{SquareArea}\n π (estimated) = 4 * {CircleArea}/{SquareArea} = {pie}')
    plt.show()
        
#call out functions
start = time.time()
plotPoints()
CalcPi()
end = time.time()
plotGraph()

#print out final statements
print(f'Number of points plotted within circle of radius of 1 = {CircleArea} \nNumber of total points plotted in the square containing circle radius of 1 = {SquareArea} \nPi equals to (estimated) = 4 * {CircleArea} / {SquareArea} = {pie} \nTime taken for execution: {end-start} seconds')
