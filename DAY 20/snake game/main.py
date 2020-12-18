import turtle as t
from snake import Snake
from food import Food
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Arcade Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
