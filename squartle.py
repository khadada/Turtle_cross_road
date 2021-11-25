from turtle import Turtle
STEP_DISTANCE = 20


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.setheading(90)
        self.goto(0, -220)

    def move_up(self):
        if self.ycor() < 220:
            self.goto(0, self.ycor() + STEP_DISTANCE)

    def move_down(self):
        if self.ycor() > -220:
            self.goto(0, self.ycor() - STEP_DISTANCE)

    def level_up(self):
        self.goto(0, -220)
