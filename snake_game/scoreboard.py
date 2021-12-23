from turtle import Turtle, colormode

ALINGMENT = 'center'
FONT = ('Arial',16,'bold')

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.count = 0
        self.high_score = 0
        with open('score.txt')as score:
            self.high_score = int(score.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)    
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f'Score: {self.count} high score: {self.high_score}', align=ALINGMENT,font=FONT)
        
    def increase_cont(self):
        self.count += 1 
        self.update_score()
        
    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
        with open('score.txt','w') as score:
            score.write(f'{self.high_score}')
        self.count = 0
        self.update_score()    
        
            