# create the play area - done
# draw center line - done
# make paddles - done
# make a ball\ -
# make ball move -
# make the barriers - done
# make bounce mechanic -
# make score board - done
# score board updater/points counter -
# make collision detection -
# controls (e.g., start and finish game, move paddles - paddles are done



























import turtle
import time
import random
# setup
s = turtle.Screen()
s.title("PyPong")
s.setup(width=640, height=480)
s.tracer(0, 1)
t = turtle.Turtle()
t.right(90)
centerline = turtle.Turtle()

# making center line
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

#perf counter
gameTime = time.perf_counter()
drawTime = time.perf_counter()
fpsTime = time.perf_counter()
fpsCounter = 0


# initial game state
shouldQuit = False
penDown = True
direction = "down"
p1direction = "none"
p2direction = "none"
paddlespeed = 2


# score variables
p1score = 0
p2score = 0

#Making score boards
p1scoreboard = turtle.Turtle()
p1scoreboard.penup()
p1scoreboard.goto(-160, 200)
p1scoreboard.write ("Score: 0", align="center", font=("courier", 24, "normal"))
p1scoreboard.hideturtle()
p2scoreboard = turtle.Turtle()
p2scoreboard.penup()
p2scoreboard.goto(160, 200)
p2scoreboard.write ("Score: 0", align="center", font=("courier", 24, "normal"))
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

def moveLeft():
    global direction
    direction = "left"

def moveRight():
    global direction
    direction = "right"

def p1release():
    global p1direction
    p1direction = "none"

def p2release():
    global p2direction
    p2direction = "none"

def doQuit():
    global shouldQuit
    shouldQuit = True

# register listeners
s.listen()
s.onkeypress(p1moveUp, "w")
s.onkeypress(p1moveDown, "s")
s.onkeypress(p2moveUp, "Up")
s.onkeypress(p2moveDown, "Down")
s.onkeypress(moveLeft, "a")
s.onkeypress(doQuit, "q")
s.onkeypress(moveRight, "d")
s.onkeyrelease(p1release, "w")
s.onkeyrelease(p1release, "s")
s.onkeyrelease(p2release, "Up")
s.onkeyrelease(p2release, "Down")

while shouldQuit == False:
    tickTime = time.perf_counter()
    if penDown:
        t.pendown()
    else:
        t.penup()
    y = p1paddle.ycor()
    if p1direction == "up":

        if y < 160:
            p1paddle.sety(y + paddlespeed)
    elif p1direction == "down":
        if y > -225:
            p1paddle.sety(y - paddlespeed)
    y = p2paddle.ycor()
    if p2direction == "up":

        if y < 160:
            p2paddle.sety(y + paddlespeed)
    elif p2direction == "down":
        if y > -225:
            p2paddle.sety(y - paddlespeed)


    if (tickTime - gameTime) > 0.1:
        gameTime = tickTime
        penDown = not penDown

    if (tickTime - drawTime) > (1/60):
        #t.fd(2)
        drawTime = tickTime

    time.sleep(1/100)
    s.update()
    fpsCounter = fpsCounter + 1

    if (tickTime - fpsTime) > 1:
        print(fpsCounter)
        fpsCounter = 0
        fpsTime = tickTime
