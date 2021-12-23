from turtle import Turtle,Screen
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

turtle = Turtle()
class Snake:
    
    def __init__(self) -> None:
        self.parts = []
        self.coords = [(0,0),(-20,0),(-40,0)]
        self.create_parts()
        self.head = self.parts[0]
        
    def create_parts(self):    
        for p in self.coords:
            self.add_segment(p)
        
    def add_segment(self,position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.speed('fast')
        snake.setpos(position)
        self.parts.append(snake)
        
    def extend(self):
        self.add_segment(self.parts[-1].position())        
        
    def move(self):
        for turtle_num in range(len(self.parts) - 1,0,-1):
            new_x = self.parts[turtle_num - 1].xcor()
            new_y = self.parts[turtle_num - 1].ycor()
            self.parts[turtle_num].goto(new_x,new_y)
        self.parts[0].forward(20)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def reset(self):
        for i in self.parts:
            i.goto(1000,1000)
        self.parts.clear()
        self.create_parts()
        self.head = self.parts[0]
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)       
            