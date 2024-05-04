from turtle import Turtle

class Player(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("turtle")
        self.speed(10000)
        self.penup()
        self.left(90)
        self.goto(x=0, y=-255)