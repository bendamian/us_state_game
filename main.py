import turtle

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)

answer_state = screen.textinput(title="Guess a state", prompt="Enter a state name?")
print(answer_state)

turtle.mainloop()
