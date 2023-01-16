from turtle import Turtle
FONT = ("Arias", 14, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.points = 0
        self.write(f"Score: {self.points}", align="center", font=FONT)

    def increase_score(self):
        self.points += 1
        self.clear()
        self.write(f"Score: {self.points}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arias", 18, "bold"))