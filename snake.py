from turtle import Turtle
SNAKE_STARTING_LENGTH = 3
MOVE_DISTANCE = 20
SNAKE_THICKNESS = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.construct()
        self.head = self.segments[0]

    def add_segment(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def construct(self):
        for i in range(SNAKE_STARTING_LENGTH):
            seg_position = (-i * SNAKE_THICKNESS, 0)
            self.add_segment(seg_position)

    def grow(self):
        seg_pos = self.segments[-1].pos()
        self.add_segment(seg_pos)

    def move(self):
        target = self.head.pos()
        self.head.fd(MOVE_DISTANCE)
        for i in range(1, len(self.segments)):
            new_target = self.segments[i].pos()
            self.segments[i].goto(target)
            target = new_target

    def north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)