from turtle import Screen, Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 50)


