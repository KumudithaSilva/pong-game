from turtle import Screen, Turtle
from ball import Ball
from boundarynet import BoundaryNet
from gamemanager import GameManager
from paddle import Paddle
from  scoreboard import  Scoreboard
import time

WINNING_SCORE = 5

# TODO 1: Create the screen
screen = Screen()
screen.register_shape("left_paddle.gif")
screen.register_shape("right_paddle.gif")
screen.register_shape("pong_ball.gif")
screen.bgpic("pong_background.gif")

screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

boundary_net = BoundaryNet()
scoreboard = Scoreboard()

# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

paddle_left.shape("left_paddle.gif")
paddle_right.shape("right_paddle.gif")

# TODO 4: Create the ball and make it move
ball = Ball()
ball.shape("pong_ball.gif")

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

manager = GameManager(ball, boundary_net, paddle_left, paddle_right, scoreboard)


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

    if scoreboard.l_score >= WINNING_SCORE or scoreboard.r_score >= WINNING_SCORE:
        game_is_on = False
        if scoreboard.l_score == scoreboard.r_score:
            winner = "It's a Draw"
        else:
            winner = "A" if scoreboard.l_score > scoreboard.r_score else "B"
        manager.game_over(winner)

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