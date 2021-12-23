from turtle import Turtle, colormode


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_cord = 10
        self.y_cord = 10
        
    def move(self):
        new_x = self.xcor() + self.x_cord
        new_y = self.ycor() + self.y_cord
        self.goto(new_x,new_y)
        
    def move_conversely(self):
        new_x = self.xcor() - self.x_cord
        new_y = self.ycor() - self.y_cord
        self.goto(new_x,new_y)    
        
    def bounce_y(self):
        self.y_cord *= -1
            
    def bounce_x(self):
        self.x_cord *= -1    
