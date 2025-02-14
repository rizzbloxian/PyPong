# 8C Vincent Tsui Retro Ping Pong


#Game rules:
#player 2 plays with F and V and Player 2 plays with up and down arrow keys.
#get a point by getting the ball to hit the other side.
#First player to get 10 points wins


# create the play area - done
# draw center line - done
# make paddles - done
# make a ball\ - done
# make ball move - done
# make the barriers - done
# make bounce mechanic - done
# make score board - done
# score board updater/points counter - done
# make collision detection - done
# controls (e.g., start and finish game, move paddles - paddles are done
# make ball go faster after certain amount of ticks
# make ball go faster based off of points ( + 1 speed every 2 points)
# add sound effects
# make game pause/end after one person reaches 10 points = done
# make middle part of paddles to make ball temporarily faster

import turtle
import time
import random
# setup
s = turtle.Screen()
s.title("PyPong")
s.setup(width=640, height=480)
s.tracer(0)

# initial game state
shouldQuit = False
p1direction = "none"
p2direction = "none"
paddlespeed = 7
ballspeed = 8


# making center line
centerline = turtle.Turtle()
centerline.penup()
centerline.goto(0, 240)
centerline.pendown()
centerline.right(90)
for x in range(48):
    if x % 2 == 0:
        centerline.pendown()
    else:
        centerline.penup()
    centerline.fd(10)
centerline.hideturtle()


# score variables
p1score = 0
p2score = 0
maxscore = 100


#Making score boards
p1scoreboard = turtle.Turtle()
p1scoreboard.penup()
p1scoreboard.goto(-160, 200)
p1scoreboard.write ("Player 1: 0", align="center", font=("courier", 20, "normal"))
p1scoreboard.hideturtle()
p2scoreboard = turtle.Turtle()
p2scoreboard.penup()
p2scoreboard.goto(160, 200)
p2scoreboard.write ("Player 2: 0", align="center", font=("courier", 20, "normal"))
p2scoreboard.hideturtle()


# creating top and bottom barriers
bottombarrier = turtle.Turtle()
bottombarrier.width(5)
bottombarrier.penup()
bottombarrier.goto(-320, -230)
bottombarrier.pendown()
bottombarrier.fd(640)
topbarrier = turtle.Turtle()
topbarrier.width(5)
topbarrier.penup()
topbarrier.goto(-320, 240)
topbarrier.pendown()
topbarrier.fd(640)

# making paddles
paddlewidth = 10
paddlelength = 75
brush = turtle.Turtle()
brush.begin_poly()
brush.begin_fill()
brush.fd(paddlewidth)
brush.rt(90)
brush.fd(paddlelength)
brush.rt(90)
brush.fd(paddlewidth)
brush.rt(90)
brush.fd(paddlelength)
brush.end_fill()
brush.end_poly()
paddle = brush.get_poly()
turtle.register_shape("paddle", paddle)
brush.clear()
brush.hideturtle()

p1paddle = turtle.Turtle()
p1paddle.shape("paddle")
p1paddle.penup()
p1paddle.rt(90)
p1paddle.goto(-310, 0)

p2paddle = turtle.Turtle()
p2paddle.shape("paddle")
p2paddle.penup()
p2paddle.rt(90)
p2paddle.goto(310, 0)

def p1moveUp():
    global p1direction
    p1direction = "up"

def p1moveDown():
    global p1direction
    p1direction = "down"

def p2moveUp():
    global p2direction
    p2direction = "up"

def p2moveDown():
    global p2direction
    p2direction = "down"

def p1release():
    global p1direction
    p1direction = "none"

def p2release():
    global p2direction
    p2direction = "none"

# register listeners
s.listen()
s.onkeypress(p1moveUp, "f")
s.onkeypress(p1moveDown, "v")
s.onkeypress(p2moveUp, "Up")
s.onkeypress(p2moveDown, "Down")
s.onkeyrelease(p1release, "f")
s.onkeyrelease(p1release, "v")
s.onkeyrelease(p2release, "Up")
s.onkeyrelease(p2release, "Down")

# making ball
ball = turtle.Turtle()
ball.shape("circle")
ball.turtlesize(0.5)
ball.right(random.randrange(-45, 45))
ball.penup()

# making bounce mechanic

while True:
    p1y = p1paddle.ycor()
    if p1direction == "up":
        if p1y < 160:
            # makes sure the paddle doesnt go through the ceiling
            p1paddle.sety(p1y + paddlespeed)
    elif p1direction == "down":
        if p1y > -225:
            # checks if paddle is under the ground
            p1paddle.sety(p1y - paddlespeed)
    p2y = p2paddle.ycor()
    if p2direction == "up":
        if p2y < 160:
            p2paddle.sety(p2y + paddlespeed)
    elif p2direction == "down":
        if p2y > -225:
            p2paddle.sety(p2y - paddlespeed)
    bally = ball.ycor()
    heading = ball.heading()
    if bally >= 230:
        ball.setheading(360 - heading)
    if bally <= -225:
        ball.setheading(360 - heading)
    x = ball.xcor()
    heading = ball.heading()
    if x >= 300:
        if (bally > p2y ) and  bally < (p2y + paddlelength):
            ball.setheading(180 - heading)
        else:
            # adds score to p1 when ball touches other side of screen
            p1score += 1
            p1scoreboard.clear()
            p1scoreboard.write (("Player 1: " + str(p1score)), align="center", font=("courier", 20, "normal"))
            ball.home()
            ball.clear()
            ball.setheading(random.randrange(135, 225))
    if x <= -310:
        if (bally > p1y ) and  bally < (p1y + paddlelength):
            ball.setheading(180 - heading)
        else:
            # adds score to p2 when ball touches other side of screen
            p2score += 1
            p2scoreboard.clear()
            p2scoreboard.write (("Player 2: " + str(p2score)), align="center", font=("courier", 20, "normal"))
            ball.home()
            ball.clear()
            ball.setheading(random.randrange(-45, 45))
    if p1score >= maxscore:
        s.clearscreen()
        s.bgcolor ("black")
        winscreen = turtle.Turtle()
        winscreen.hideturtle()
        winscreen.pencolor("white")
        winscreen.write(("Congratulations! Player 1 Wins!"), align="center", font=("courier", 25, "normal"))
        s.update()
        break
    if p2score >= maxscore:
        s.clearscreen()
        s.bgcolor("black")
        winscreen = turtle.Turtle()
        winscreen.hideturtle()
        winscreen.pencolor("white")
        winscreen.write(("Congratulations! Player 2 Wins!"), align="center", font=("courier", 25, "normal"))
        s.update()
        break

    ball.fd(ballspeed)
    s.update()

    time.sleep(1/60)




