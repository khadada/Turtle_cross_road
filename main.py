from turtle import Screen
from time import sleep
from squartle import Timmy
from cars import Car
screen = Screen()
screen.listen()
screen.setup(600, 500)
timmy = Timmy()
screen.onkey(timmy.move_up, 'Up')
screen.onkey(timmy.move_down, 'Down')
car = Car()
screen.tracer(0)
while True:
    screen.update()
    sleep(.1)
    car.create_car()
    car.move()



screen.exitonclick()
