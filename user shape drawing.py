#turtle_drawingShapes by Joon Hao, built in Visual Studio Code

#import
import turtle

#create window
window = turtle.Screen()

#speed of pen
turtle.speed(2)

#user input size, sides
size = int(window.textinput('Size', 'How big do you want your shape to be: '))
sides = int(window.textinput('Sides', 'How many sides do you want your shape to have: '))
turtle_shape = str(window.textinput('Shape of pen', 'What type of pen would you like: '))
#shape of pen
turtle.shape(turtle_shape)

#user fill/pen preference input
user_fillOrPen = str(window.textinput('Fill or Pen', "Would you like to fill the shape with a colour or just outline ('fill', 'pen'): "))

#def function to draw shape
def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360 / sides)


#start of draw based on user preference
if user_fillOrPen == 'fill':
    shape_fill_colour = str(window.textinput('Colour of shape', 'What fill colour for your shape would you like: '))
    #colour of fill
    turtle.color(shape_fill_colour)

    turtle.begin_fill()
    shape(size, sides)
    turtle.end_fill()

    #ending message
    turtle.penup()
    turtle.hideturtle()
    turtle.sety(200)
    turtle.write(f'Ta da! Your {size} pixel size, {sides} sides shape drawn by {turtle_shape} with {shape_fill_colour} filled in!', False, align="center", font=("Arial", 15, "normal"))

elif user_fillOrPen == 'pen':
    pen_colour = str(window.textinput('Colour of pen', 'What colour pen would you like: '))

    #colour of pen
    turtle.color(pen_colour)
    
    shape(size, sides)

    #ending message
    turtle.penup()
    turtle.hideturtle()
    turtle.sety(200)
    turtle.write(f'Ta da! Your {size} pixel size, {sides} sides shape drawn by {turtle_shape} with {pen_colour} outline!', False, align="center", font=("Arial", 15, "normal"))

else:
    window.textinput('Error', 'No such command')


#window exit only when user clicks on it
window.exitonclick()
