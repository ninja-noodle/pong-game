from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.pu()
        self.setpos(x_pos, 0)
        self.shapesize(5, 1)
        self.color("white")

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)


