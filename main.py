import turtle
from turtle import Screen
from time import sleep
from random import randint

from player import Player
from cars import Cars

screen = Screen()

screen.setup(width=1000, height=600)
screen.title("Turtle Crossing - by Raphael Manayon")
screen.tracer(0)

cars = Cars()
player = Player()

game = True

def move():

    player.forward(5)

screen.listen()

screen.onkeypress(key="w", fun=move)
screen.onkeypress(key="Up", fun=move)

while game:
    sleep(0.1)
    if randint(1, 3) == 1:
        cars.spawn_car()
    for car in cars.cars:
        car.forward(cars.speed/2)
        if car.xcor() + car.shapesize()[1] * 9 >= player.xcor() - 10 >= car.xcor() - car.shapesize()[1] * 9:
            if car.ycor() + 9 >= player.ycor() >= car.ycor() - 9:
                game = False
    if player.ycor() >= 255:
        sleep(3)
        cars.increase_difficulty()
        player.goto(x=0, y=-255)

    screen.update()

screen.exitonclick()