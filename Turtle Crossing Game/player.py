from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)  # set the turtle head face up
        self.reset_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)  # turtle move up speed

    def reset_position(self):
        self.goto(STARTING_POSITION)  # back to the original position

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True  # true if turtle touch the top (ycor = 280)
        else:
            return False  # false if turtle not touch the top (ycor = 280)
