from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle misses
# TODO 7: Keep score

# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

# TODO 4: Create the ball and make it move
ball = Ball()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

# TODO 4: Create the ball and make it move
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()



screen.exitonclick()