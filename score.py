from turtle import Turtle
from config import FONT, BOARD


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as high_score: 
            self.high_score = high_score.read()
        self.penup()
        self.hideturtle()
        self.goto(0, (BOARD / 2) - 25)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.points}", align="center", font=FONT)

    def increase_score(self):
        self.points += 1
        self.clear()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "r") as high_score: 
                high_score.write(self.high_score) 
        self.score = 0
        self.update_score()