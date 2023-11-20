from turtle import Screen, Turtle
from paddles import Paddle
from ball import BallObj
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = BallObj()


screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")


game_status = True
while game_status:
    time.sleep(0.1)
    ball.directions(right_paddle, left_paddle)
    ball.move()
    screen.update()


screen.exitonclick()
