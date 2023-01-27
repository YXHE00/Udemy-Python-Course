import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# # get the x and y coor when click the screen
# def get_mouse_click_coor(x, y):  # take 2 values and print out
#     print(x, y)
# # event listener, listen for when the mouse clicks, then it's going to call get_mouse_click_coor
# turtle.onscreenclick(get_mouse_click_coor)
# # alternative way of keeping screen open, even though code has finished running
# turtle.mainloop()
# # result shows on 50_states.csv

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="what's another state's name?").title()  # make the first letter capitalized

    # if user type "exit", the game will exit
    if answer_state == "Exit":
        # the name of states which have not guessed by the user when they exit the game
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # generate a new csv file to save all of missing states
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # if answer_state is one of the states in all the states
    if answer_state in all_states:
        guessed_states.append(answer_state)  # add answer_state inside the guessed_states list
        # create a new turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # go to the position where the user correctly guessed the state coor
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())  # answer_state

screen.exitonclick()
