import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("black")
screen.setup(width=600, height=400)

# Create turtles
player_turtle = turtle.Turtle()  # Corrected: Added parentheses
player_turtle.pencolor("red")
player_turtle.shape("turtle")
player_turtle.penup()
player_turtle.goto(-250, 50)

enemy_turtle = turtle.Turtle()  # Corrected: Added parentheses
enemy_turtle.pencolor("blue")
enemy_turtle.shape("turtle")
enemy_turtle.penup()
enemy_turtle.goto(-250, 0)  # Adjusted position for clarity

def move_up():
    y = player_turtle.ycor()
    if y < 150:
        player_turtle.sety(y + 20)

def move_down():
    y = player_turtle.ycor()
    if y > -150:
        player_turtle.sety(y - 20)

def move_left():
    x = player_turtle.xcor()
    if x > -250:
        player_turtle.setx(x - 20)

def move_right():
    x = player_turtle.xcor()
    if x < 250:
        player_turtle.setx(x + 20)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Race function
def race():
    while player_turtle.xcor() < 250 and enemy_turtle.xcor() < 250:
        enemy_move = random.randint(1, 5)
        enemy_turtle.forward(enemy_move)

        player_turtle.forward(3)

    if player_turtle.xcor() >= 250:
        print("You win!")
    else:
        print("You lose!")

# Start the race with a key press
screen.onkey(race, "space")  # Press space to start the race

# Finish up
screen.mainloop()





