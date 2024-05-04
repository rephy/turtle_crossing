from turtle import Turtle
from time import sleep

class MainMessages(Turtle):

    def __init__(self):

        super().__init__()
        self.speed(10000)
        self.hideturtle()

    def game_over(self):

        self.forward(0)
        self.write("Game over!", align="center", font=("Comic Sans MS", 80, "normal"))

    def new_difficulty(self, current_difficulty, screen):

        self.forward(0)
        self.write(f"Passed Level {current_difficulty}!", align="center", font=("Comic Sans MS", 80, "normal"))
        screen.update()
        sleep(3)
        self.clear()
        self.write(f"Proceeding to level {current_difficulty + 1}...", align="center", font=("Comic Sans MS", 80, "normal"))
        screen.update()
        sleep(3)
        self.clear()