from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []  # create a car list
        self.car_speed = STARTING_MOVE_DISTANCE  # set the car speed

    def create_car(self):
        random_chance = random.randint(1, 6)  # a new car generate every 6 times random
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # set the car size as wide 20, length 40
            new_car.penup()  # remove the line when car move
            new_car.color(random.choice(COLORS))  # random color from color list
            random_y = random.randint(-240, 240)  # random ycor position
            new_car.goto(300, random_y)  # create new car original position
            self.all_cars.append(new_car)  # add new car to the car list

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # move from right to left is backward

    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # when level up, car speeds increase
