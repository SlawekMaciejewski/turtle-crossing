import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.colormode(255)
screen.title("The turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.ycor() == 280:
        player.start_position()

screen.exitonclick()
