from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-220, 260)  # on top-left of the screen
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # everytime clear the previous level
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)  # show the highest level on the screen

    def increase_score(self):
        self.score += 1  # increase the level
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)  # show on the center of the screen
        self.write("GAME OVER", align=ALIGN, font=FONT)
