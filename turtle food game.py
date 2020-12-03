    #turtle food game by bjh-developer, built in Visual Studio code, with Python 3

    #import modules
    import turtle, random, time
    from turtle import heading, setheading, speed, write

    #init pens and screen
    window = turtle.Screen()
    referee = turtle.Pen()
    player = turtle.Pen()
    target = turtle.Pen()
    timerpen = turtle.Pen()
    scorepen = turtle.Pen()
    referee.speed(0)
    score = 0
    timer = 30
    window.tracer(0)
    target.shape('circle')
    target.color('red')
    target.pu()
    target.seth(random.randint(0, 360))
    player.shape('turtle')
    player.color('dark green')
    player.seth(180)
    player.pu()
    p_speed = 0.3
    window.colormode(255)
    window.bgcolor('cyan')
    window.title('Turtle food game!')

    #ask user if ready
    user_ready = window.textinput('Instructions for game', '1. change direction of\nyour turtle with left/right\nkeys\n\n2. change speed of turtle\nwith up/down keys\n\n3. eat food 15 times\nunder 30 sec to win\n\nAre you READY? (Y/N)')

    #create game field
    def field():
        global timer
        global score
        referee.color('black')
        referee.width('4')
        referee.pu()
        referee.setpos(-150, -250)
        referee.pd()
        referee.setpos(150, -250)
        referee.setpos(150, 250)
        referee.setpos(-150, 250)
        referee.setpos(-150, -250)
        timerpen.pu()
        timerpen.setpos(130, 255)
        timerpen.hideturtle()
        timerpen.write(f'Timer: {timer}', align='center', font=('Comic Sans', 15, "normal"))
        scorepen.pu()
        scorepen.setpos(-130, 255)
        scorepen.hideturtle()
        scorepen.write(f'Score: {score}', align='center', font=('Comic Sans', 15, "normal"))
        referee.pu()
        referee.setpos(-370, -100)
        referee.pd()
        referee.write('Instructions for game:\n\n1. change direction of\nyour turtle with left/right\nkeys\n\n2. change speed of turtle\nwith up/down keys\n\n3. eat food 15 times\nunder 30 sec to win', move=False, align='left', font=['Arial', 15, 'normal'])
        referee.hideturtle()

    #def boundaries and ricochet pen based on the law of reflection
    def ricochet(object):
        if object.xcor() <= -150:
            if object.heading() >= 90  and object.heading() <= 180:
                object.setheading(90 - (object.heading() - 90)) 
            elif object.heading() <= 270 and object.heading() >= 180:
                object.setheading(270 + (270 - object.heading()))
            else:
                pass
        elif object.xcor() >= 150:
            if object.heading() >= 270 and object.heading() <= 360:
                object.setheading(270 - (object.heading() - 270))
            elif object.heading() <= 90 and object.heading() >= 0:
                object.setheading(90 - (object.heading() - 90))
            else:
                pass
        elif object.ycor() <= -250:
            if object.heading() >= 270 and object.heading() <= 360:
                object.setheading(90 - (object.heading() - 270))
            elif object.heading() <= 270 and object.heading() >= 180:
                object.setheading(90 + (270 - object.heading()))
            else:
                pass
        elif object.ycor() >= 250:
            if object.heading() >= 0 and object.heading() <= 90:
                object.setheading(270 + (90 - object.heading()))
            elif object.heading() <= 180 and object.heading() >= 90:
                object.setheading(270 - (object.heading() - 90))
            else:
                pass
        else:
            pass

    #init keys to instruct pen to move and its speed
    def left():
        player.left(15)
    def right():
        player.right(15)
    def increase_speed():
        global p_speed
        if p_speed <= 0.6:
            p_speed += 0.1
        else:
            pass
    def decrease_speed():
        global p_speed
        if p_speed >= 0.2:
            p_speed -= 0.1
        else:
            pass

    #start game
    def game():
        while timer > 0 and score < 15:
            #events
            window.listen()
            window.onkey(left, 'Left')
            window.onkey(right, 'Right')
            window.onkey(increase_speed, 'Up')
            window.onkey(decrease_speed, 'Down')
            ricochet(target)
            ricochet(player)
            player.forward(p_speed)
            target.forward(0.3)
            if dist() < 20:
                target.setpos(random.randint(-150, 150), random.randint(-250, 250))
                target.seth(random.randint(0, 360))
                update_score()
            if int(time.time() - start_time) != 30 - timer:
                countdown()
            if score == 15:
                referee.pu()
                referee.setpos(340, 0)
                referee.pd()
                referee.write('Congratulations!\nYou have won!', move=False, align='right', font=['Arial', 15, 'normal'])
                referee.hideturtle()
            elif timer == 0 and score < 15:
                referee.pu()
                referee.setpos(355, 0)
                referee.pd()
                referee.write('Sadly, you have lost :(', move=False, align='right', font=['Arial', 15, 'normal'])
                referee.hideturtle()
            window.update()



    #init countdown timer
    def countdown():
        global timer
        timer -= 1
        timerpen.undo()
        timerpen.write(f'Timer: {timer}', align='center', font=('Comic Sans', 15, "normal"))

    #sets up detection of turtle eating food
    def dist():
        xdist = player.xcor() - target.xcor()
        ydist = player.ycor() - target.ycor()
        distance = (xdist ** 2 + ydist ** 2) ** 0.5
        return distance

    #init scores
    def update_score():
        global score
        score += 1
        scorepen.undo()
        scorepen.write(f'Score: {score}', align='center', font=('Comic Sans', 15, "normal"))



    #call
    field()
    start_time = time.time()
    i = 0
    while i == 0:
        if user_ready == 'Y' or user_ready == 'y' or user_ready == "yes" or user_ready == 'Yes':
            i = 1
            while i == 1:
                game()
                window.exitonclick()
        elif user_ready == 'N' or user_ready == 'n' or user_ready == "no" or user_ready == 'No':
            i = 2
            pass
        else:
            window.textinput('ERROR', 'Sorry, that input is not recognised, please try again')
            user_ready = window.textinput('Instructions for game', '1. change direction of\nyour turtle with left/right\nkeys\n\n2. change speed of turtle\nwith up/down keys\n\n3. eat food 15 times\nunder 30 sec to win\n\nAre you READY? (Y/N)')