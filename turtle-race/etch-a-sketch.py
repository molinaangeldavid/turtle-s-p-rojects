from turtle import Turtle, Screen, colormode


def validate_option()->int:
    option = input('Enter how do you like draw (1. keys or 2. mouse): ')
    while not (option.isnumeric() and int(option) == 1 or int(option) == 2):
        option = input('Error !!. Enter a valid choice (1. keys or 2. mouse): ')
    option = int(option)
    return option 
    
bob = Turtle()
screen = Screen()

def go_forward():
    bob.forward(10)
    
def go_backward():
    bob.backward(10)
    
def turn_clockwise():
    bob.right(5)
    
def turn_counter_clockwise():
    bob.left(5)
    
def clean_screen():
    bob.clear()
    bob.home()
    bob.clear()

def main():
    bob.pensize(3)
    colormode(255)
    bob.pencolor((23,100,87))
    screen.onkeypress(fun=go_forward,key='w')
    screen.onkeypress(fun=go_backward,key='s')
    screen.onkeypress(fun=turn_clockwise,key='d')
    screen.onkeypress(fun=turn_counter_clockwise,key='a')
    screen.onkeypress(fun=clean_screen,key='c')
    screen.listen()
    screen.exitonclick()

main()