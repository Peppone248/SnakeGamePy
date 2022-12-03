from turtle import Turtle
from food import Food
from main import food


class Scoreboard(Turtle):

    def __init__(self):
        super.__init__()
        self.write("Score: " + str(food.counter) + " ", False, align="center")

