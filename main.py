from turtle import Screen
from ball import Ball
from paddle import Paddle
from  scoreboard import  Scoreboard
import time

# TODO 1: Create the screen
screen = Screen()
scoreboard = Scoreboard()
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
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 5: Detect collision with wall and bounce
    if ((ball.distance(paddle_right) < 50 and ball.xcor() > 320)
            or (ball.distance(paddle_left) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        game_is_on = False

    # TODO 6: Detect collision with paddle misses
    # TODO 7: Keep score
    if ball.xcor() > 380:
        scoreboard.left_score()
        scoreboard.update_scoreboard()
        ball.reset_position()

    if ball.xcor() <- 380:
        scoreboard.right_score()
        scoreboard.update_scoreboard()
        ball.reset_position()

    screen.update()



screen.exitonclick()