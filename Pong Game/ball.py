from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # reverse the y coordination direction

    def bounce_x(self):
        self.x_move *= -1  # reverse the x coordination direction
        self.move_speed *= 0.9  # each time the ball touch the paddle will increase it speed.

    def reset_position(self):
        self.goto(0, 0)  # when reset the game, ball goes back to original position
        self.move_speed = 0.1  # when reset the game, the ball speeds back to 0.1
        self.bounce_x()  # when reset the game, ball goes to reverse paddle
