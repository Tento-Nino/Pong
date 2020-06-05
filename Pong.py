# Simple Pong in Python 3
# By Nino LoPiccolo
# Make sound avalible on Linux Chromebook
# Figure out game start -- Space button as start

import turtle
import os
score_a = 0
score_b = 0

wn = turtle.Screen()
wn.title("Pong by Nino LoPiccolo")
wn.bgcolor("orange")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(50)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(50)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(100)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2
ball.shapesize(stretch_wid=.5, stretch_len=.5)
# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 18, "bold"))

bottom_box = turtle.Turtle()
bottom_box.speed(0)
bottom_box.color("white")
bottom_box.penup()
bottom_box.hideturtle()
bottom_box.goto(0, 230)
bottom_box.write("Don't Fuck Up", align="center", font=("Courier", 10, "bold"))


#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_up, "w")


#Main Game Loop
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay ping_pong_8bit_plop.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay ping_pong_8bit_plop.wav")

# Boarder checking for Paddles

    if paddle_b.ycor() < -240:
        paddle_b.sety(-235)

    if paddle_b.ycor() > 240:
        paddle_b.sety(240)
        
    if paddle_a.ycor() < -240:
        paddle_a.sety(-235)
    
    if paddle_a.ycor() > 240:
        paddle_a.sety(240)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 18, "bold"))
        bottom_box.clear()
        bottom_box.write("Holy Fuck!", align="center", font=("Courier", 10, "bold"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 18, "bold"))
        bottom_box.clear()
        bottom_box.write("Holy Shit, Man!", align="center", font=("Courier", 10, "bold"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay ping_pong_8bit_plop.wav")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay ping_pong_8bit_plop.wav")
