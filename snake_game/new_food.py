from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('DarkOrchid')
        self.speed('fastest')
        self.new_position()
        
    def new_position(self):
        set_x = random.randint(-285,285)
        set_y = random.randint(-285,245)
        self.goto(set_x,set_y)