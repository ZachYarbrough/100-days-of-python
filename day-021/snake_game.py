from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
score = 0

snake = Snake()
food = Food()

game_is_on = True

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")


while game_is_on:
    screen.update()
    time.sleep(0.01)
    snake.move()

    if snake.head.distance(food) < 15:
        score += 1
        food.refresh()
        snake.add_segment()
    

screen.exitonclick()