import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.title("The turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
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

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.xcor() == -320: # deleting unused cars
            car_manager.all_cars.remove(car)
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.start_position()
        scoreboard.increase_level()

screen.exitonclick()
