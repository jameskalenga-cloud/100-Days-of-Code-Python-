from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")





turtles = []
distance = -20


for index in range(0,3):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(x=distance*index, y=0)
    turtles.append(tuple)






















screen.exitonclick()