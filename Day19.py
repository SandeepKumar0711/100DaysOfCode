from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_color = screen.textinput(title="make your Bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]

turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    turtle_list.append(new_turtle)
if user_color:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_color:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
