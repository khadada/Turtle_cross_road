from turtle import Turtle
import random
COLORS = ["RoyalBlue", "PeachPuff", "MintCream", "SlateBlue",
          "Khaki", "OliveDrab", "BurlyWood", "LightSalmon", "Coral", "HotPink",
          "LemonChiffon", "AliceBlue", "LightGrey", "MediumTurquoise", "DarkSeaGreen",
          "Peru", "Tomato", "Orchid", "PapayaWhip"]

MOVE_DISTANCE = 5


class Car:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        num = random.randint(1, 6)
        if num == 1:
            car = Turtle('square')
            car.shapesize(1.2, 2.8)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-180, 180)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)

