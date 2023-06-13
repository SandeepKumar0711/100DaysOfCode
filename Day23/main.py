import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Cross The Road")

tim = Player()
cars = CarManager()
score = Scoreboard()

game_is_on = True
screen.listen()
screen.onkeypress(tim.move, "Up")
loop_count = 0

while game_is_on:
    time.sleep(0.1)
    cars.move_car()

    cars.generate_cars()
    screen.update()

    for car in cars.all_cars:
        if car.distance(tim) < 20:
            score.game_over()
            game_is_on = False

    if tim.crossed_finish_line():
        tim.goto_start()
        cars.level_up()
        score.update_scoreboard()

screen.exitonclick()