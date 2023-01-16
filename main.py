#imports
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#create new snake
snake = Snake()
#new food
food = Food()
#scoreboard
score = Score()

#listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#game on bool
game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collisions
    #food collision
    if snake.head.distance(food) < 15:
        food.respawn()
        score.increase_score()
        snake.extend_snake()

    #wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game = False
        score.game_over()

    #body collision
    for section in snake.sections[1:]:
        if snake.head.distance(section) < 10:
            game = False
            score.game_over()


screen.exitonclick()