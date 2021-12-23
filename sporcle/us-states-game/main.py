import turtle,pandas
# Must be a .gif file
IMAGE = 'blank_states_img.gif'
FILE = '50_states.csv'

def opencsv(pos)->tuple:
    data = pandas.read_csv(FILE)
    state = data[data['state'] == pos]
    x = int(state.x)
    y = int(state.y)
    return (x,y)
    
def states()->list:    
    data = pandas.read_csv(FILE)
    state = data['state']
    state = state.to_list()
    return state

def save_csv(states):
    states = {'states':list(states)}
    states = pandas.DataFrame(states)
    states.to_csv('missing_states.csv')
    
screen = turtle.Screen()
state = turtle.Turtle()
state.penup()
state.ht()


screen.title('U.S State Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)
guessed = []
all_states = states()
count = 0
while len(guessed) < 50:
    answer_state = screen.textinput(title=f'{count}/50 States correct ', prompt='What\'s the state name?')
    answer_state = answer_state.title()
    if answer_state == 'Exit':
        states_miss = set(all_states) - set(guessed)
        save_csv(states_miss)
        break    
    
    while not answer_state in all_states:
        answer_state = screen.textinput(title=f'{count}/50 States correct ', prompt='What\'s the state name?')
        answer_state = answer_state.title()
    position = opencsv(answer_state)
    if len(position) > 0 and not answer_state in guessed:
        guessed.append(answer_state)
        count += 1
        state.goto(position)
        state.write(arg=f'{answer_state}',font=('Arial',6,'bold'))
    else:
        pass
    