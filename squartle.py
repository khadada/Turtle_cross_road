from turtle import Turtle


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.setheading(90)
        self.goto(0, -220)
