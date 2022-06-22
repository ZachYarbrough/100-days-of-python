from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_racing = False
turtle_selected = screen.textinput(title="Choose your turtle!", prompt="Enter a color:")

all_turtles = []

timmy = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
tammy = Turtle(shape="turtle")
bob = Turtle(shape="turtle")
steve = Turtle(shape="turtle")

def setup(turtle, yCord, color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=yCord)
    all_turtles.append(turtle)

setup(timmy, -100, "red")
setup(tammy, -50, "orange")
setup(tommy, 0, "yellow")
setup(bob, 50, "green")
setup(steve, 100, "blue")

if turtle_selected:
    is_racing = True


while is_racing:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            winning_turtle = turtle.pencolor()
            if winning_turtle == turtle_selected:
                print(f"You won! The winning turtle was the {winning_turtle} turtle!")
            else:
                print(f"You lost! The winning turtle was the {winning_turtle} turtle!")
            is_racing = False
            break
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
    

screen.exitonclick()