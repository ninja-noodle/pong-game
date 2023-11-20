from turtle import Turtle


class BallObj(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.setpos(0, 0)
        self.x_direction = 1
        self.y_direction = 1

    def directions(self, pr, pl):
        if self.ycor() >= 280:
            self.y_direction = -1
        elif self.ycor() <= -280:
            self.y_direction = 1
        elif self.distance(pr) < 30:
            self.x_direction = -1
        elif self.distance(pl) < 30:
            self.x_direction = 1

    def move(self):
        if self.x_direction == 1:
            if self.y_direction == -1:
                self.goto(self.xcor() + 8, self.ycor() - 10)
            elif self.y_direction == 1:
                self.goto(self.xcor() + 8, self.ycor() + 10)
        elif self.x_direction == -1:
            if self.y_direction == -1:
                self.goto(self.xcor() - 8, self.ycor() - 10)
            elif self.y_direction == 1:
                self.goto(self.xcor() - 8, self.ycor() + 10)
