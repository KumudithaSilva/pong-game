from turtle import Screen, Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
GAME_OVER_FONT = ("Courier", 35, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 240)
        self.write(f"Player A : {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(150, 240)
        self.write(f"Player B : {self.r_score}", align=ALIGNMENT, font=FONT)

    def left_score(self):
        self.l_score += 1

    def right_score(self):
        self.r_score += 1

    def game_over(self, winner):
        self.goto(0,0)
        self.write(f"Player {winner} Wins!", align=ALIGNMENT, font=GAME_OVER_FONT)