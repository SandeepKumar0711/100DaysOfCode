from turtle import Turtle

FONT = ('Courier', 72, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    # def winner(self):
    #     if self.r_score > 6:
    #         self.goto(0, 0)
    #         self.write(f"Player-2 Wins!!!", False, font=FONT)
    #         return False
    #     elif self.l_score > 6:
    #         self.goto(0, 0)
    #         self.write(f"Player-1 Wins!!!", False, font=FONT)
    #         return False
