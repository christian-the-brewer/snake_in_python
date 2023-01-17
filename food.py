from turtle import Turtle
from config import FOOD_ZONE
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-FOOD_ZONE, FOOD_ZONE), random.randint(-FOOD_ZONE, FOOD_ZONE))

    def respawn(self):
        self.goto(random.randint(-FOOD_ZONE, FOOD_ZONE), random.randint(-FOOD_ZONE, FOOD_ZONE))