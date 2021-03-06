from turtle import Screen
from time import sleep
from squartle import Timmy
from cars import Car
from score import Score
screen = Screen()
screen.listen()
screen.setup(600, 500)
timmy = Timmy()
screen.onkey(timmy.move_up, 'Up')
screen.onkey(timmy.move_down, 'Down')
car = Car()
score = Score()
screen.tracer(0)
game_is_on = True
while game_is_on:
    screen.update()
    sleep(car.speed_car)
    car.create_car()
    car.move()
    for ca in car.all_cars:
        if timmy.distance(ca) < 20:
            score.game_over()
            game_is_on = False
    if timmy.is_at_finish_line():
        print('You win')
        score.score_up()
        timmy.go_to_start()
        car.gas()


screen.exitonclick()
