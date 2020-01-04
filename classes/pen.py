import turtle


class Pen:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.score_a = 0
        self.score_b = 0
        self.create_pen()
        self.write_score()

    def create_pen(self):
        self.pen.color('white')
        self.pen.speed(0)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)

    def write_score(self):
        self.pen.clear()
        self.pen.write(f'Player A: {self.score_a}   Player B: {self.score_b}', align='center',
                       font=('Courier', 24, 'normal'))

    def increment_score(self, incr_a, incr_b):
        self.score_a += incr_a
        self.score_b += incr_b
        self.write_score()
