import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set the screen size and title
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")

# turn off the tracer
screen.tracer(0)

# import player, scoreboard and car_manager class
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# keystrokes that going to listen for the up key
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create cars on the screen and the cars are auto move from right to left
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
