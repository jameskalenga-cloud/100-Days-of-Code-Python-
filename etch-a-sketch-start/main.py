from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

position =-100

turtle_race_rod_wave =  []

for turtle_color in colors:
    turtle = Turtle("turtle")
    turtle.color(turtle_color)
    turtle.penup()
    turtle.goto(x=-230, y=position)
    position +=  35
    turtle_race_rod_wave.append(tuple)





screen.exitonclick()
