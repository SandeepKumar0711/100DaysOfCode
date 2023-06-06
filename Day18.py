from turtle import Screen
import turtle as t
import random

color_list = [(29, 106, 164), (227, 158, 66), (231, 214, 93), (188, 42, 84), (219, 139, 173), (139, 105, 59),
              (29, 106, 164), (227, 158, 66), (231, 214, 93), (188, 42, 84), (219, 139, 173), (139, 105, 59),
              (114, 185, 211), (216, 73, 99), (200, 167, 33), (159, 24, 65), (113, 191, 156), (24, 54, 129),
              (16, 182, 152), (105, 108, 192), (141, 208, 227), (236, 89, 50), (20, 139, 89), (230, 164, 185),
              (20, 167, 207), (99, 49, 38), (81, 42, 30), (24, 43, 79), (23, 90, 85), (239, 213, 6), (153, 214, 199),
              (26, 84, 90)]

timmy_the_turtle = t.Turtle()
t.colormode(255)
timmy_the_turtle.speed('fastest')
timmy_the_turtle.setheading(225)
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
timmy_the_turtle.pendown()
x = timmy_the_turtle.xcor()
y = timmy_the_turtle.ycor()
for _ in range(10):
    for _ in range(10):
        timmy_the_turtle.color(random.choice(color_list))
        timmy_the_turtle.dot(20)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
    y = y + 50.0
    timmy_the_turtle.setpos(x, y)

screen = Screen()
screen.exitonclick()
