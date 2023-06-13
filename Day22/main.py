from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
pong_ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(pong_ball.ball_speed)
    screen.update()
    pong_ball.move_ball()
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320:
        pong_ball.bounce_x()

    if pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    if pong_ball.xcor() > 380:
        pong_ball.ball_reset()
        score.l_point()
        # game_is_on = score.winner()
    if pong_ball.xcor() < -380:
        pong_ball.ball_reset()
        score.r_point()
        # game_is_on = score.winner()
screen.exitonclick()
