#imports
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#size of snake at start
starting_size = 3

#snake body
snake = []

#game on bool
game = True

#create first three snake parts
starting_x = 0
for _ in range(0,starting_size):
    new_section = Turtle(shape="square")
    new_section.color("white")
    new_section.penup()
    new_section.goto(x=starting_x, y=0)
    starting_x -= 20
    snake.append(new_section)

head = snake[0]

def move_snake():
    for section_number in range(len(snake) - 1, 0, -1):
        new_x = snake[section_number - 1].xcor()
        new_y = snake[section_number - 1].ycor()
        snake[section_number].goto(new_x, new_y)

while game:
    screen.update()
    time.sleep(0.1)
    head.fd(20)
    head.right(90)
    head.fd(20)
    head.fd(20)
    head.fd(20)
    head.fd(20)
    head.right(90)
    head.fd(20)
    head.fd(20)
    head.fd(20)

#creates new segment
def grow_snake():
    """Adds section to snake"""
    #move each section to position of previous section

screen.exitonclick()