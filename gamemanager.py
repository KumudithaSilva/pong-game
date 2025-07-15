import time

class GameManager:
    def __init__(self, ball, net, paddle_left, paddle_right, scoreboard):
        self.ball = ball
        self.net = net
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.scoreboard = scoreboard

    def hide_game_objects(self):
        self.ball.hideturtle()
        self.net.clear()
        self.net.hideturtle()

    def game_over(self, winner):
        self.paddle_left.goto((-350, 0))
        self.paddle_right.goto((350, 0))
        self.ball.hideturtle()
        self.net.clear()
        self.net.hideturtle()
        time.sleep(0.5)
        self.scoreboard.game_over(winner)
