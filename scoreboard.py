from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write("Score: " + str(self.score) + " ", align="center", font=("Montserrat", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Montserrat", 30, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write("Score: " + str(self.score) + " ", align="center", font=("Arial", 20, "normal"))



