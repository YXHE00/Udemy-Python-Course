from turtle import Turtle
import random

# render itself as a small circle on the screen
# everytime the snake touches the food, then that food is going to move to a new random location


class Food(Turtle):

    def __init__(self):
        super().__init__()  # food class inheritance from Turtle class
        self.shape("circle")  # food class shape as circle
        self.penup()  # pen up, no line appear after food move
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # default is 20 pixel. len and wid = 20 * 0.5 = 10 pixel
        self.color("blue")  # set the circle color to blue
        self.speed("fastest")  # set the circle speed
        self.refresh()  # when call Food class in main.py, the screen appear a random circle

    def refresh(self):
        random_x = random.randint(-280, 280)  # random x coordination, make sure the circle not touch the boarder
        random_y = random.randint(-280, 280)  # random y coordination, make sure the circle not touch the boarder
        self.goto(random_x, random_y)  # circle go to a new random location
