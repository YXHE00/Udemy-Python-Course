from turtle import Turtle

# set the format, keep constants
ALIGN = "center"
FONT = ("Arial", 24, "normal")


# scoreboard is going to be a turtle which knows how to keep track of the score and display on the screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # set the initial point as 0
        self.color("white")  # set the scoreboard color
        self.penup()  # pen up before goto the position
        self.goto(0, 270)  # set the score at top middle location
        self.hideturtle()  # hide the arrow, only display the self.write()
        self.update_scoreboard()  # when call scoreboard class in main.py, the scoreboard appear on the screen

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)  # score display on screen

    def game_over(self):
        self.goto(0, 0)  # as default set goto top middle, the end sign need at center of the screen
        self.write("GAME OVER", align=ALIGN, font=FONT)  # game over sign

    def increase_score(self):
        self.score += 1  # each time score increase 1
        self.clear()  # to clear the previous test that was written on the screen
        self.update_scoreboard()  # score update on screen

