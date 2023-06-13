from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.goto(x_cor, y_cor)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        if self.ycor() < 260:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -260:
            self.sety(self.ycor() - 20)
