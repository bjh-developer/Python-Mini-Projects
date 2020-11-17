#turtle_drawingShapes by Joon Hao, built in Visual Studio Code

#import
import turtle

#create window
window = turtle.Screen()

#user input size, sides
size = int(window.textinput('Size', 'How big do you want your shape to be: '))
sides = int(window.textinput('Sides', 'How many sides do you want your shape to have: '))
turtle_shape = str(window.textinput('Shape of pen', 'What type of pen would you like: '))
pen_colour = str(window.textinput('Colour of pen', 'What colour pen would you like: '))

#speed of pen
turtle.speed(2)

#shape of pen
turtle.shape(turtle_shape)

#colour of pen
turtle.color(pen_colour)

#def function to draw shape
def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360 / sides)

shape(size, sides)
turtle.penup()
turtle.hideturtle()
turtle.sety(200)
turtle.write(f'Ta da! Your {size} pixel size, {sides} sides shape drawn by {turtle_shape} with {pen_colour}!', False, align="center", font=("Arial", 15, "normal"))

#window exit only when user clicks on it
window.exitonclick()