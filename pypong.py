# create the play area - done
# draw center line - done
# make paddles -
# make a ball\ -
# make ball move -
# make the barriers - done
# make bounce mechanic -
# make score board - done
# score board updater/points counter -
# make collision detection -
# controls (e.g., start and finish game, move paddles -



























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

def moveUp():
    global direction
    direction = "up"

def moveDown():
    global direction
    direction = "down"

def moveLeft():
    global direction
    direction = "left"

def moveRight():
    global direction
    direction = "right"

def doQuit():
    global shouldQuit
    shouldQuit = True

# register listeners
s.listen()
s.onkeypress(moveUp, "w")
s.onkeypress(moveDown, "s")
s.onkeypress(moveLeft, "a")
s.onkeypress(moveRight, "d")
s.onkeypress(doQuit, "q")


while shouldQuit == False:
    tickTime = time.perf_counter()
    if penDown:
        t.pendown()
    else:
        t.penup()

    if direction == "up":
        t.setheading(90)
    elif direction == "down":
        t.setheading(270)
    elif direction == "left":
        t.setheading(180)
    elif direction == "right":
        t.setheading(0)

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
