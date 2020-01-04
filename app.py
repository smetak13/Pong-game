import turtle
from classes.paddle import Paddle
from classes.ball import Ball

wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = Paddle(-350)

# Paddle B
paddle_b = Paddle(350)

# Ball
ball = Ball()

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a.move_up, 'w')
wn.onkeypress(paddle_a.move_down, 's')
wn.onkeypress(paddle_b.move_up, 'Up')
wn.onkeypress(paddle_b.move_down, 'Down')


# Main game loop
while True:
    wn.update()

    # Get paddle coordinates
    paddle_a_xcor = paddle_a.get_xcor()
    paddle_a_ycor = paddle_a.get_ycor()
    paddle_b_xcor = paddle_b.get_xcor()
    paddle_b_ycor = paddle_b.get_ycor()

    # Ball logic
    ball.move()
    ball.check_borders()
    ball.check_panel_collision(
        paddle_a_xcor, paddle_a_ycor, paddle_b_xcor, paddle_b_ycor)
