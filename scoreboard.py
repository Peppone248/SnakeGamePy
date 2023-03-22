from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.score = 0
            with open("data.txt", "r") as f:
                self.high_score = int(f.read())
            self.penup()
            self.goto(0, 270)
            self.color("white")
            self.hideturtle()
            self.update_scoreboard()

        def update_scoreboard(self):
            self.clear()
            self.write("Score: " + str(self.score) + " High Score: " + str(self.high_score), align="center",
                       font=("Montserrat", 20, "normal"))

        def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("data.txt", 'w') as f:
                    f.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()

        def update_score(self):
            self.score += 1
            self.update_scoreboard()
