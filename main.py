from turtle import Screen
from squartle import Timmy
screen = Screen()
screen.listen()
screen.setup(600, 500)
timmy = Timmy()
screen.onkey(timmy.move_up, 'Up')
screen.onkey(timmy.move_down, 'Down')
screen.exitonclick()
