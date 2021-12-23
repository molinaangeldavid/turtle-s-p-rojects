from turtle import Turtle

class Border(Turtle):
    
    def __init__(self):
        super().__init__()
        
    def create_border(self, position, heading, forward):
        border = Turtle()
        border.color("cyan")
        border.ht()
        border.penup()
        border.pensize(width=2)
        border.goto(position)
        border.pendown()
        border.setheading(heading)
        border.forward(forward)
    
    def create_borders(self):
        # Right Border
        self.create_border((290,250), 270, 540)
        # Left Border
        self.create_border((-290, 250), 270, 540)
        # UP Border
        self.create_border((-290, 250), 0, 580)
        # Down Border
        self.create_border((-290, -290), 0, 580)    