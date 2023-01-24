from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)   # screen size
screen.bgcolor("black")       # set background colour
screen.title("My Snake Game")   # title of the window that shows up
screen.tracer(0)  # turn off the tracer - turn turtle animation off

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# keystrokes that going to listen for are up, down, left, right arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake automatically across the screen
game_is_on = True

while game_is_on:
    screen.update()  # set the time delay before something get update, argument to the screen.tracer()
    time.sleep(0.1)  # used to slow the animation check each segment move

    # game start and move the snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # if the distance between snake and food is less than 15
        food.refresh()  # the food refresh to the new location
        snake.extend()  # snake body extend when touch the food
        scoreboard.increase_score()  # scoreboard increase 1

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # trigger game over
        scoreboard.game_over()  # display game over sign

    # detect collision with tail
    for segment in snake.segments[1:]:  # for loop each segment(except the first segment) in snake body
        if snake.head.distance(segment) < 10:  # if head(first segment) and any other segments distance less than 10
            game_is_on = False  # trigger game over
            scoreboard.game_over()  # display game over sign

screen.exitonclick()  # When it run, it doesn't just disappear straight away
