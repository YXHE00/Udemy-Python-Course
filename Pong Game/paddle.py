from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")  # set the paddle shape as square with 20 * 20 pixel
        self.color("white")  # set the paddle color as white
        self.shapesize(stretch_wid=5, stretch_len=1)  # paddle width is 100 and length is 20 pixel
        self.penup()  # when paddle move, not leave any lines behind
        self.goto(x_cor, y_cor)  # move to this position standby

    # press up button to move up 20 pixel to the new position
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # press down button to move down 20 pixel to the new position
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
