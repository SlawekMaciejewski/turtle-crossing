import time
from turtle import Screen
from player import Player
from car_manager import Car

screen = Screen()
screen.title("The turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() == 280:
        player.start_position()

screen.exitonclick()
