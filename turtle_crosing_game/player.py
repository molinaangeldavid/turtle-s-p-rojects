from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        
    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def move_right(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)
        self.left(90)
        
    def reset_position(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)
                    
            