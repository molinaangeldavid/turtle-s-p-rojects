from turtle import Screen, left
from bar_player import Bar
from ball import Ball
from score import Score,Line
import time


screen = Screen()
screen.setup(1000,800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

player_1 = Bar((-450,0),(69, 89, 214))
player_2 = Bar((450,0),(27, 169, 5))
ball = Ball()
score = Score()
line = Line()

screen.listen() 
screen.onkeypress(player_1.move_up,key='w')
screen.onkeypress(player_1.move_down,key='s')
screen.onkeypress(player_2.move_up,key='Up')
screen.onkeypress(player_2.move_down,key='Down')

game_on = True
orientation = 'right'
line.vertical_line()
screen.update()
speed = 0.1
while game_on:
    screen.update()
    time.sleep(speed)
    if score.score_1 == 0 and score.score_2 == 0 or orientation == 'right':
        ball.move()
        
    if orientation == 'left':
        ball.move_conversely() 
        
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.distance(player_2) < 50 and ball.xcor() > 420 or ball.distance(player_1) < 50 and ball.xcor() < -420:
        ball.bounce_x()
        speed /= 1.2
        
    if ball.xcor() > 440:
        speed = 0.1
        score.lose_player2()
        ball.hideturtle()
        ball.home()
        ball.showturtle()
        orientation = 'left'
        
    if ball.xcor() < -440:
        speed = 0.1
        score.lose_player1()
        ball.hideturtle()
        ball.home()
        ball.showturtle()
        orientation = 'right'
        
    if score.score_1 > 10 or score.score_2 > 10:    
        game_on = False
        ball.ht()
        line.clear()        
        if score.score_1 == 11:
            score.win_player('1')
        elif score.score_2 == 11:
            score.win_player('2')

screen.exitonclick()