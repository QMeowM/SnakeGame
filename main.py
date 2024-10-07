from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.north, key="Up")
screen.onkey(fun=snake.south, key="Down")
screen.onkey(fun=snake.east, key="Right")
screen.onkey(fun=snake.west, key="Left")

"""turn off animation"""
screen.tracer(0)
game_on = 1
while game_on:

    snake.move()
    """update position of elements on screen"""
    time.sleep(.1)
    screen.update()

# detect collision with wall
    if not (-390 < snake.segments[0].xcor() < 390 and -290 < snake.segments[0].ycor() < 290):
        game_on = 0
        score.game_over()

# Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        score.update()
        snake.grow()

# detect collision with body
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_on = 0
#             score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = 0
            score.game_over()




screen.exitonclick()