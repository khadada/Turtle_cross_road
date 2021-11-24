from turtle import Turtle
FONT = ('Courier', 17, 'normal')
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('Black')
        self.score = 0
        self.goto(0, 180)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Your score: {self.score}', align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align=ALIGNMENT, font=FONT)
