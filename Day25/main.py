import pandas
import turtle

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "download.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
all_state = state_data.state.to_list()
correct_guess = []


score = 0
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="what's another state's name?").title()
    if answer_state == 'Exit':
        left_state = [i for i in all_state if i not in correct_guess]
        left_guesses = pandas.DataFrame({'State Name': left_state})
        left_guesses.to_csv("Data.csv", index= False)
        break
    if answer_state in all_state:
        correct_guess.append(answer_state.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        found = state_data[state_data.state == answer_state]
        t.goto(int(found.x), int(found.y))
        t.write(answer_state)
        score += 1
