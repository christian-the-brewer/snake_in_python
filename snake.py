#imports
from turtle import Turtle
from config import STARTING_SIZE, MOVEMENT

class Snake:
    def __init__(self):
        self.sections = []
        self.create_snake()
        self.head = self.sections[0]
        self.tail = self.sections[-1]

    def create_snake(self):
        starting_x = 0
        starting_x_y = (starting_x, 0)
        for _ in range(0,STARTING_SIZE):
            self.add_section(starting_x_y)
            starting_x -= 20
            
    def move(self):
        for section_number in range(len(self.sections) - 1, 0, -1):
            new_x = self.sections[section_number - 1].xcor()
            new_y = self.sections[section_number - 1].ycor()
            self.sections[section_number].goto(new_x, new_y)
        self.head.fd(MOVEMENT)

    #directional controls
    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def add_section(self, position):
        new_section = Turtle(shape="square")
        new_section.color("white")
        new_section.penup()
        #new_section.goto(x=starting_x, y=0)
        new_section.goto(position)
        
        self.sections.append(new_section)

    def extend_snake(self):
        self.add_section(self.tail.position())

    def reset_snake(self):
        for section in self.sections:
            section.goto(600, 600)
        self.sections.clear()
        self.create_snake()
        self.head = self.sections[0]
        self.tail = self.sections[-1]
    