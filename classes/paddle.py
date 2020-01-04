import turtle


class Paddle:
    def __init__(self, location):
        self.location = location
        self.paddle = turtle.Turtle()
        self.create_paddle()

    def create_paddle(self):
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.goto(self.location, 0)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        y = self.paddle.ycor()
        y += 20
        if y > 240:
            y = 240
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 20
        if y < -240:
            y = -240
        self.paddle.sety(y)

    def get_xcor(self):
        return self.paddle.xcor()

    def get_ycor(self):
        return self.paddle.ycor()
