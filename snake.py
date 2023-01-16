#imports
from turtle import Turtle

#starting size of snake
starting_size = 3

#movement speed(distance)
MOVEMENT = 20

class Snake:
    def __init__(self):
        self.sections = []
        self.create_snake()

    def create_snake(self):
        starting_x = 0
        for _ in range(0,starting_size):
            new_section = Turtle(shape="square")
            new_section.color("white")
            new_section.penup()
            new_section.goto(x=starting_x, y=0)
            starting_x -= 20
            self.sections.append(new_section)

    def move(self):
        for section_number in range(len(self.sections) - 1, 0, -1):
            new_x = self.sections[section_number - 1].xcor()
            new_y = self.sections[section_number - 1].ycor()
            self.sections[section_number].goto(new_x, new_y)
        self.sections[0].fd(MOVEMENT)

    def up(self):
        self.sections[0].seth(90)

    def down(self):
        self.sections[0].seth(270)

    def left(self):
        self.sections[0].seth(180)

    def right(self):
        self.sections[0].seth(0)