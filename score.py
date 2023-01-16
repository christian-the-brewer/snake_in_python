from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 275)
        self.penup()
        self.color("white")
        self.points = 0
        self.write(f"Score: {self.points}", align="center", font=("Arias", 14, "normal"))

    def increase_score(self):
        self.points += 1
        self.clear()
        self.write(f"Score: {self.points}", align="center", font=("Arias", 14, "normal"))