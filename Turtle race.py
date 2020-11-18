# turtle race by bjh-developer, built in Visual Studio code, with Python 3

#import
from random import gammavariate
import turtle, random

#init screen
window = turtle.Screen()
window.colormode(255)

#init pen (racer & referee)
racer1 = turtle.Pen()
racer2 = turtle.Pen()
racer3 = turtle.Pen()
referee = turtle.Pen()
referee.speed(0)

#global var
global game
game = False

#ask for name
racer1_name = window.textinput('Racer 1', 'What name do you want for racer 1?')
racer2_name = window.textinput('Racer 2', 'What name do you want for racer 2?')
racer3_name = window.textinput('Racer 3', 'What name do you want for racer 3?')


#def field
def field():
    referee.color('dark green')
    referee.begin_fill()
    referee.setpos(-200, -300)
    referee.setpos(-200, 300)
    referee.setpos(200, 300)
    referee.setpos(200, -300)
    referee.setpos(-200, -300)
    referee.end_fill()


#def get_ready
def set_up():
    #make last line
    referee.pu()
    referee.setpos(70, -300)
    referee.pd()
    referee.color('white')
    referee.width('3')
    referee.setpos(70, 300)

    #make first line
    referee.pu()
    referee.setpos(-70, -300)
    referee.pd()
    referee.color('white')
    referee.width('3')
    referee.setpos(-70, 300)

    #make finish line
    referee.pu()
    referee.setpos(200, 280)
    referee.pd()
    referee.color('red')
    referee.width('3')
    referee.setpos(-200, 280)

    #make referee invisible
    referee.hideturtle()


#def get ready 
def get_ready():
    #set racer to start position
    racer1.setpos(-130, -290)
    racer2.setpos(0, -290)
    racer3.setpos(140, -290)

    #set racer to face front
    racer1.seth(90)
    racer2.seth(90)
    racer3.seth(90)

    #set racer to be turtle
    racer1.shape('turtle')
    racer2.shape('turtle')
    racer3.shape('turtle')

    #set racer's colours
    racer1.color('cyan')
    racer2.color('yellow')
    racer3.color('purple')


#def race
def race():
    global game
    while not game:
        #racer move forward
        racer1.forward(random.randint(10, 20))
        racer2.forward(random.randint(10, 20))
        racer3.forward(random.randint(10, 20))

        #racer turn
        racer1.left(random.randint(-10, 10))
        racer2.left(random.randint(-10, 10))
        racer3.left(random.randint(-10, 10))

        #checking boundary
        check_boundaries()

        #check win
        referee.pu()
        referee.setpos(0, 0)
        if racer1.ycor() >= 280:
            referee.write(f'Congrats!\n{racer1_name} won!', move=False, align="center", font=("Arial", 25, "normal"))
            game = True
        elif racer2.ycor() >= 280:
            referee.write(f'Congrats!\n{racer2_name} won!', move=False, align="center", font=("Arial", 25, "normal"))
            game = True 
        elif racer3.ycor() >= 280:
            referee.write(f'Congrats!\n{racer3_name} won!', move=False, align="center", font=("Arial", 25, "normal"))
            game = True
        else:
            pass


#def boundaries
def check_boundaries():
    if racer1.xcor() <= -200:
        racer1.seth(70)
    elif racer1.xcor() >= -70:
        racer1.seth(100)
    if racer2.xcor() <= -70:
        racer2.seth(70)
    elif racer2.xcor() >= 70:
        racer2.seth(100)
    if racer3.xcor() <= 70:   
        racer3.seth(70)
    elif racer3.xcor() >= 200:
        racer3.seth(100)



#call
field()
set_up()
get_ready()
race()


window.exitonclick()