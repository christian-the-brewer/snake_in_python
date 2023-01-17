# Snake
A remake of the classic in everyone's favorite serpentine programming language, Python!

## Overview
The game is played by using the arrow keys to move the snake around and eat the blocks of food that appear randomly. Make sure to avoid running into the walls or your own body!

# Config
There are seven configurable variables in the game, which can be found in the config.py file:
* **STARTING_SIZE**: Sets the lenght of the snake at start.
* **MOVEMENT**: Sets how far the snake moves each frame.
* **SPEED**: Sets the speed of game by adjusting delay between each frame with time.sleep(). A lower value increases game speed.
* **BOARD**: Sets height and width of payable area.
* **FOOD_ZONE**: Sets area for food to spawn. NOTE: automatically set by **BOARD**.
* **BOUNDRY**: Sets x and y coordinates to detect collisions. NOTE: automatically set by **BOARD**.
* **FONT**: Sets font and size of scoreboard.

## Libraries
This game imports three libraries:
* **[turtle](https://docs.python.org/3/library/turtle.html#turtle.write)**: Used for creating game screen and all animations.
* **[random](https://docs.python.org/3/library/random.html?highlight=random#module-random)**: Used to generate pseudo- random numbers to spawn food.
***[time](https://docs.python.org/3/library/time.html?highlight=time#module-time)**: Used to set a framerate.


