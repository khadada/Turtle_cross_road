from turtle import Turtle
import random
COLORS = ["RebeccaPurple", "RoyalBlue", "PeachPuff", "MintCream", "SlateBlue",
          "Khaki", "OliveDrab", "BurlyWood", "LightSalmon", "Coral", "HotPink",
          "LemonChiffon", "AliceBlue", "LightGrey", "MediumTurquoise", "DarkSeaGreen",
          "Peru", "Tomato", "Orchid", "PapayaWhip"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color("black")
        self.shapesize(1.8, 3.8)
        self.penup()
        self.color(random.choice(COLORS))
        # position
