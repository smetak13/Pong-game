import turtle
import os
from classes.pen import Pen
from random import randint


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.default_speed = 2
        self.ball.dx = self.default_speed
        self.ball.dy = self.default_speed
        self.pen = Pen()
        self.create_ball()

    def create_ball(self):
        self.ball.speed(0)
        self.ball.shape('square')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def check_borders(self):
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            self.play_sound('bounce')

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            self.play_sound('bounce')

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.pen.increment_score(1, 0)
            self.play_sound('hooray')
            self.reset_ball_speed()

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.pen.increment_score(0, 1)
            self.play_sound('hooray')
            self.reset_ball_speed()

    def check_panel_collision(self, paddle_a_xcor, paddle_a_ycor, paddle_b_xcor, paddle_b_ycor):
        if self.ball.xcor() > 340 and self.ball.xcor() < 350 and self.ball.ycor() < paddle_b_ycor + 50 and self.ball.ycor() > paddle_b_ycor - 50:
            self.ball.setx(340)
            self.ball.dx *= -1
            self.play_sound('pong')
            self.increment_ball_speed(0.05, True)

        if self.ball.xcor() < -340 and self.ball.xcor() > -350 and self.ball.ycor() < paddle_a_ycor + 50 and self.ball.ycor() > paddle_a_ycor - 50:
            self.ball.setx(-340)
            self.ball.dx *= -1
            self.play_sound('pong')
            self.increment_ball_speed(0.05, False)

    def play_sound(self, sound):
        os.system(f'afplay sounds/{sound}.wav&')

    def increment_ball_speed(self, incr, is_negative):
        random_offset_x = randint(1, 7) / 100
        random_offset_y = randint(1, 7) / 100
        if is_negative:
            self.ball.dx -= incr + random_offset_x
            self.ball.dy -= incr + random_offset_y
        else:
            self.ball.dx += incr + random_offset_x
            self.ball.dy += incr + random_offset_y
        print(self.ball.dx, self.ball.dy)
        print(random_offset_x, random_offset_y)

    def reset_ball_speed(self):
        self.ball.dx = self.default_speed
        self.ball.dy = self.default_speed
