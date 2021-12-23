from turtle import Turtle,Screen
import random

colors = ['cyan','pink','red','orange','yellow','brown']
screen = Screen()
screen.screensize(canvheight=800,canvwidth=800)
set_bet = screen.textinput('Which turtle\'s will win', 'Please input the colour of the turtle: ')
is_race_on = True
y_pos = -350
turtles_users = []

# def user_bet():
for turtle_user in range(6):
    y_pos += 100
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_user])
    new_turtle.penup()
    new_turtle.goto(-380,y_pos)
    turtles_users.append(new_turtle)
    
while is_race_on:
    for t in turtles_users:
        if t.xcor() > 390:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == set_bet:
                print(f'You\'ve won! The {winning_color} turtle is the winner')
            else:
                print(f'You\'ve losed! The {winning_color} turtle is the winner')
                    
        move_random = random.randint(0,10)
        t.forward(move_random)
        
            
screen.exitonclick()