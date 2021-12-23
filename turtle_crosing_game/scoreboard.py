from turtle import Turtle, left, update


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.ht()
        self.goto(-200,260)
        self.update_score()

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_score()
        
    def update_score(self):
        self.write(f'Level: {self.level}',align='center',font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,30)
        self.write('GAME OVER',align='center',font=FONT)
        self.home()
        self.update_score()    
            