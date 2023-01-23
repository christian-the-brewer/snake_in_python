from turtle import Turtle
from config import FONT, BOARD


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as high_score: 
            self.high_score = int(high_score.read())
        self.penup()
        self.hideturtle()
        self.goto(0, (BOARD / 2) - 25)
        self.color("white")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align="center", font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score: 
                high_score.write(str(self.high_score)) 
        self.score = 0
        self.update_score()