import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up,'Up')
screen.onkeypress(player.move_down,'Down')
screen.onkeypress(player.move_left,'Left')
screen.onkeypress(player.move_right,'Right')

game_is_on = True
while game_is_on:
    car.create_cars()
    time.sleep(0.1)
    screen.update()    
    car.move()
    if player.ycor() > 280:
        player.reset_position()
        score.level_up()
        car.increase_speed()
    for c in car.cars:
        if c.distance(player) < 20:
            game_is_on = False
            score.game_over()
            car.increase_speed()
        
screen.exitonclick()
