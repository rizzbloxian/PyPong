import turtle
import time

# setup
s = turtle.Screen()
s.title("PyPong")
s.setup(width=640, height=480)
s.tracer(0, 1)
t = turtle.Turtle()
t.right(90)

gameTime = time.perf_counter()
drawTime = time.perf_counter()
fpsTime = time.perf_counter()
fpsCounter = 0


# initial game state
shouldQuit = False
penDown = True
direction = "down"

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
        t.fd(1)
        drawTime = tickTime

    time.sleep(0.0)
    s.update()
    fpsCounter = fpsCounter + 1

    if (tickTime - fpsTime) > 1:
        print(fpsCounter)
        fpsCounter = 0
        fpsTime = tickTime
