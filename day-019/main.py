from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def counter_clockwise():
    timmy.left(15)
    timmy.forward(10)

def clockwise():
    timmy.right(15)
    timmy.forward(10)

def clear():
    screen.reset()
    timmy.color('green')

timmy.shape('turtle')
timmy.color('green')

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()