#imports
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

#size of snake at start
starting_size = 3

#snake body
snake = []

#create first three snake parts
starting_x = 0
for _ in range(0,starting_size):
    new_body = Turtle(shape="square")
    new_body.color("white")
    new_body.goto(x=starting_x, y=0)
    starting_x -= 20


#creates new segment
def grow_snake():
    """Adds section to snake"""

screen.exitonclick()