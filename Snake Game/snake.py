from turtle import Turtle

# set the starting position for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# set the move distance to 20 to keep all move constants
MOVE_DISTANCE = 20
# set the head turn position to keep constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []  # create a new list for snake body
        self.create_snake()  # when call the Snake class in main.py, the snake body appear
        self.head = self.segments[0]  # set head as first element in the segments list

    # Create a snake body with 3 segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # create 3 position for snake body, start form centre and move left

    # add one segment
    def add_segment(self, position):
        new_segment = Turtle("square")  # set the snake body as square
        new_segment.color("white")  # set the body color
        new_segment.penup()  # when square move won't draw any line
        new_segment.goto(position)  # the body start within 3 positions connect to each other
        self.segments.append(new_segment)  # append the square to the snake body list

    # add a new segment to the end of the snake body
    def extend(self):
        self.add_segment(self.segments[-1].position())  # .position is the method from turtle class

    # move the last segment position to the first segment position
    def move(self):
        # seg_num start from end of the snake body list, end at segments[0], step=-1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # set new x coordinate as previous segment position
            new_y = self.segments[seg_num - 1].ycor()  # set new y coordinate as previous segment position
            self.segments[seg_num].goto(new_x, new_y)  # the last segment will goto previous segment position
        self.segments[0].forward(MOVE_DISTANCE)  # snake list first position need move forward 20 pixel each time

    # control the snake head position
    def up(self):
        if self.head.heading() != DOWN:  # if the heading go down, not allow go up
            self.head.setheading(UP)  # the head (first segment) turn left 90 degree - go up

    def down(self):
        if self.head.heading() != UP:  # if the heading go up, not allow go down
            self.head.setheading(DOWN)  # the head (first segment) turn left 270 degree - go down

    def left(self):
        if self.head.heading() != RIGHT:  # if the heading go right, not allow go left
            self.head.setheading(LEFT)  # the head (first segment) turn left 180 degree - go left

    def right(self):
        if self.head.heading() != LEFT:  # if the heading go left, not allow go right
            self.head.setheading(RIGHT)  # the head (first segment) turn left 0 degree - go right
