from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scorebord import Scorebord
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scorebord=Scorebord()
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 54 or ball.distance(l_paddle)<50 and ball.xcor()< -320:
        ball.x_bounce()

    if ball.xcor()>380:
        ball.reset_position()
        scorebord.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scorebord.r_point()


screen.exitonclick()
