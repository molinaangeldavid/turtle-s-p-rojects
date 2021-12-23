from turtle import Turtle, position
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_s = STARTING_MOVE_DISTANCE
        self.ht()
        self.penup()
        self.goto(500,500)
        
    def create_cars(self):
        random_number = random.randint(1,5)
        if random_number == 1:
            car = Turtle()
            car.shape('square')
            car.penup()
            car.turtlesize(stretch_len=1.5,stretch_wid=1)
            car.setheading(180)
            self.random_position(car)
            color_car = random.choice(COLORS)
            car.color(color_car)   
            self.cars.append(car)    
            
            
    def move(self):
        for i in self.cars:       
            i.forward(self.move_s)
            if i.xcor() < -300:
                position_y = random.randint(-220,240)
                position_x = random.randint(300,600)
                i.goto(position_x,position_y)
                
    def random_position(self,car):
        position_y = random.randint(-220,240)
        position_x = random.randint(300,600)
        car.goto(position_x,position_y)
        
    def increase_speed(self):
        self.move_s += MOVE_INCREMENT
        