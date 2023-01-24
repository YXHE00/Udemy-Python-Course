from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # hidde the turtle graph
        self.l_score = 0  # set the left score as 0
        self.r_score = 0  # set the right score as 0
        self.update_scoreboard()  # first initialized the scoreboard

    def update_scoreboard(self):
        self.clear()  # when score update, the previous score will eliminate

        self.goto(-100, 200)  # left score position
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))

        self.goto(100, 200)  # right score position
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1  # left paddle score increase 1
        self.update_scoreboard()  # update the left paddle score on the screen

    def r_point(self):
        self.r_score += 1  # right paddle score increase 1
        self.update_scoreboard()  # update the left paddle score on the screen
