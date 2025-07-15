import turtle

class BoundaryNet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.pensize(3)
        self.draw_net()

    def draw_net(self):
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
