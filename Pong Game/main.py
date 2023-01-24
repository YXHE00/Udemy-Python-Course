from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()  # create the screen
screen.setup(width=800, height=600)  # screen size
screen.bgcolor("black")  # set background colour
screen.title("Pong Game")  # title of the window that shows up
screen.tracer(0)  # turn off the tracer - turn turtle animation off

# create a right paddle and a left paddle
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# import ball class
ball = Ball()

# import scoreboard class
scoreboard = Scoreboard()

# keystrokes that going to listen for are up and down
screen.listen()

# right paddle use up and down arrow key
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# left paddle use w and s key
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)  # control the ball move speed
    screen.update()  # turn on the tracer
    ball.move()  # make the ball move

    # detect collision with top(280 ycor) or bottom(-280 ycor) wall, ball(ycor) change direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with all paddles, ball(xcor) change direction
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect right paddle misses, left paddle get point
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle misses, right paddle get point
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

