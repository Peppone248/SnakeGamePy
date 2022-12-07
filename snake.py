from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()


class Snake:
    start_pos = [(0, 0), (-20, 0), (-40, 0)]
    segments = []

    def __init__(self):
        for pos in self.start_pos:
            self.add_tails(pos)
            self.head = self.segments[0]
            self.tail = self.segments[-1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg_num - 1].xcor()
            next_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(next_x, next_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)

    def add_tails(self, pos):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(pos)
        self.segments.append(new_snake)

    def extend(self):
        self.add_tails(self.segments[-1].position())

