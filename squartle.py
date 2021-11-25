from turtle import Turtle
STEP_DISTANCE = 20
FINISH_LINE = 180
STARTING_POSITION = (0, -220)


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        if self.ycor() < 220:
            self.goto(0, self.ycor() + STEP_DISTANCE)

    def move_down(self):
        if self.ycor() > -220:
            self.goto(0, self.ycor() - STEP_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        return False
