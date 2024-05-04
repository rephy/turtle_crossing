from turtle import Turtle, colormode
from random import randint, randrange

class Cars:

    def __init__(self):

        self.cars = []
        self.speed = 10

        colormode(255)

    def spawn_car(self):

        car = Turtle()
        car.shape("square")

        stretch = randrange(2, 5)
        color = {
            'r': randint(0, 255),
            'g': randint(0, 255),
            'b': randint(0, 255)
        }

        car.shapesize(stretch_len=stretch)
        car.color(color['r'], color['g'], color['b'])

        starting_x = 500 + (10 * stretch)
        starting_y = randint(-10, 10) * 20

        if randint(0, 1) == 1:
            starting_x *= -1

        car.penup()

        car.speed("fastest")
        car.goto(starting_x, starting_y)

        self.cars.append(car)

    def increase_difficulty(self):

        for car in self.cars:
            car.hideturtle()

        self.cars = []

        self.speed *= 1.3