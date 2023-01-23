#imports
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
from config import SPEED, BOARD, BOUNDRY
import time

screen = Screen()
screen.setup(width=BOARD, height=BOARD)
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
    time.sleep(SPEED)
    snake.move()

    #detecting collisions
    #food collision

    if snake.head.distance(food) < 15:
        food.respawn()
        score.increase_score()
        snake.extend_snake()

    #wall collision
    if snake.head.xcor() > BOUNDRY or snake.head.xcor() < -BOUNDRY or snake.head.ycor() > BOUNDRY or snake.head.ycor() < -BOUNDRY:
        snake.reset_snake()
        score.game_over()

    #body collision
    for section in snake.sections[1:]:
        if snake.head.distance(section) < 10:
            snake.reset_snake()
            score.game_over()


screen.exitonclick()