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
head = snake[0]

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


while game:
    screen.update()
    time.sleep(.1)
    for section in snake:
        section.fd(20)



#creates new segment
def grow_snake():
    """Adds section to snake"""
    #move each section to position of previous section

screen.exitonclick()