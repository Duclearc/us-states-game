import turtle
import pandas as pd

screen = turtle.Screen()

screen.title('name all 50 states'.title())
img = './blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
correct_answers = []
answer_comment = ''
states_file = pd.read_csv('./50_states.csv')


def write_state_name(x, y, state_name, font=('Arial', 12, 'normal'), color='black'):
    """writes the state_name at the specified 'x' and 'y' coordinates.
    Optionally, a font tuple and color might also be specified"""
    pen = turtle.Turtle()
    pen.ht()
    pen.color(color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(state_name, align='center', font=font)


while len(correct_answers) < 50:
    answer = screen.textinput(
        title=f'{answer_comment} {len(correct_answers)}/50',
        prompt='Name a US State:').title().strip()
    state = states_file[states_file.state == answer]
    if len(state) > 0 and answer not in correct_answers:
        answer_comment = 'CORRECT -'
        write_state_name(int(state.x), int(state.y), answer)
        correct_answers.append(answer)
    elif len(state) > 0 and answer in correct_answers:
        answer_comment = 'ALREADY IN -'
    else:
        answer_comment = 'WRONG -'

write_state_name(0, 0, 'CONGRATULATIONS! \n You\'ve named all 50 states!', ('Arial', 36, 'bold'), 'red')
screen.exitonclick()
