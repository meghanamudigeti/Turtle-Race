from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=600,height=550)

is_race_on = False
user_choice = screen.textinput(title="Make a bet",prompt="Which turtle will win the race?Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple","brown","magenta","pink","grey"]
y_positions = [-200,-150,-100,-50,0,50,100,150,200,250]
all_turtles = []

for turtle_index in range(0,10):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-280, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if user_choice == winning_turtle_color:
                print(f"You've won, the {winning_turtle_color} turtle won the race.")
            else:
                print(f"You've lost, the {winning_turtle_color} turtle won the race.")
            break
        distance = random.randint(0,10)
        turtle.speed("fastest")
        turtle.forward(distance)


screen.exitonclick()

