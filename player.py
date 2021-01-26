from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_position()

    def start_position(self):
        self.goto(0, -280)
        self.setheading(90)
