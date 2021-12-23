from turtle import Turtle, colormode

class Bar(Turtle):
    
    def __init__(self,position,color):
        super().__init__()
        self.shape('square')
        self.goto(position) 
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=0.5)
        self.penup()
        colormode(255)
        self.color(color)
        
    def move_up(self):
        self.setheading(90)
        self.forward(20)
        
    def move_down(self):
        self.backward(20)