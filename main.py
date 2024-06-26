from turtle import Screen
from time import sleep
from random import randint

from player import Player
from cars import Cars
from text import MainMessages, Level

screen = Screen()

screen.setup(width=1000, height=600)
screen.title("Turtle Crossing - by Raphael Manayon")
screen.tracer(0)

cars = Cars()
player = Player()

main_messages = MainMessages()
level_keeper = Level()

game = True

level_keeper.level(1)

def move():

    player.forward(5)

screen.listen()

screen.onkeypress(key="w", fun=move)
screen.onkeypress(key="Up", fun=move)

while game:
    sleep(0.1/cars.difficulty)
    if randint(1, 3 * 10 ** (cars.difficulty - 1)) <= 11 ** (cars.difficulty - 1):
        cars.spawn_car()
    for car in cars.cars:
        car.forward(cars.speed/2)
        if car.xcor() + car.shapesize()[1] * 9 >= player.xcor() - 10 >= car.xcor() - car.shapesize()[1] * 9:
            if (car.ycor() + 10 >= player.ycor() - 10 >= car.ycor() - 10) or (car.ycor() + 10 >= player.ycor() + 10 >= car.ycor() - 10):
                game = False
                cars.clear_cars()
                main_messages.game_over()
                
    if player.ycor() >= 255:
        cars.clear_cars()
        main_messages.new_difficulty(cars.difficulty, screen)
        cars.increase_difficulty()
        level_keeper.level(cars.difficulty)
        player.goto(x=0, y=-255)

    screen.update()

screen.exitonclick()