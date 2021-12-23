from turtle import Screen
from snake import Snake
from new_food import Food
from scoreboard import Score
from border import Border
import time
screen = Screen()
screen.setup(650,650)
screen.bgcolor('black')
screen.title('My Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
walls = Border()
walls.create_borders()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.left,'Left')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')

game_on = True
while game_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    
    wall_x = snake.head.xcor()
    wall_y = snake.head.ycor()
    
    if snake.head.distance(food) < 15:
        food.new_position()
        score.increase_cont()
        snake.extend()
        
    if wall_x >= 290 or wall_x <= -290 or wall_y > 250 or wall_y <= -290:
        score.reset()
        snake.reset()
        
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            score.reset()    
            snake.reset()
        
screen.exitonclick()