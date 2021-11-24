from turtle import Turtle


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.shapesize(1.2, 1.2)
        self.penup()
        # position
