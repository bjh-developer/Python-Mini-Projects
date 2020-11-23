#koch fractals drawing by bjh-developer, built in Visual Studio code, with python 3

#import
import turtle

#init screen and pen
window = turtle.Screen()
kochi = turtle.Pen()
kochi.speed(20)

#ask user for number of orders
order = int(window.textinput('Order', 'How many orders do you want to do for the fractal?'))

#set up to draw one order
def koch(order, size):
    if order == 0:
        kochi.forward(size)
    elif order > 0:
        koch(order - 1, size / 3)
        kochi.left(60)
        koch(order - 1, size / 3)
        kochi.right(120)
        koch(order - 1, size / 3)
        kochi.left(60)
        koch(order - 1, size / 3)

#set up to draw multiple order with the one order
def koch_snowflake(order, size):
    if order == 0:
        count = 0
        while count < 3:
            koch(order, size)
            koch.forward(size)
            koch.right(120)
            count += 1
    elif order > 0:
        koch(order - 1, size / 3)
        kochi.left(60)
        koch(order - 1, size / 3)
        kochi.right(120)
        koch(order - 1, size / 3)
        kochi.left(60)
        koch(order - 1, size / 3)

#call
koch_snowflake(order, 300)


#commands window to exit when clicked
window.exitonclick()