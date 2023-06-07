from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")
screen.update()

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
wall_coordinate = [280, -280]
while game_is_on:
    screen.update()

    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # detect collision for wall
    if snake.head.xcor() in wall_coordinate or snake.head.ycor() in wall_coordinate:
        game_is_on = False
        score.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
