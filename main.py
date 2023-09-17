from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(l_paddle.go_up, "W".lower())
screen.onkeypress(l_paddle.go_down, "S".lower())
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")



game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()











# TODO Create the screen
# TODO Create and move a paddle
# TODO Create a second paddle
# TODO Create the ball and make it move
# TODO Detect ball collision with walls and bounce
# TODO Detect ball collision with paddle
# TODO Detect when paddle misses
# TODO Keep score

