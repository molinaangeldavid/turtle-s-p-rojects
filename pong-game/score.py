from turtle import Turtle, update

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0,350)
        self.update_score()
            
    def lose_player1(self):
        self.clear()
        self.score_2 += 1
        self.update_score()
        
    def lose_player2(self):
        self.clear()
        self.score_1 += 1    
        self.update_score()
        
    def update_score(self):
        self.write(f'{self.score_1}          {self.score_2}',align='center',font=('Calibri',25,'normal'))   
        
    def win_player(self,player):
        self.clear()
        self.goto(0,0)    
        self.write(f'Win player {player}\n{self.score_1} | {self.score_2}',align='center',font=('Calibri',25,'normal'))   
        
class Line(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pensize(5)
        self.penup()    
        self.setheading(270)
                
    def vertical_line(self):
        self.goto(0,400)
        while self.ycor() > -400:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)            
            
                    