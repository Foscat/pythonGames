import turtle
import os
# import winsound #Needed fo sounds in windows

window = turtle.Screen()
window.title("Pong by Foscat")
window.bgcolor("black")
window.setup(width=800, height=600)
#Tracer keeps window from updating and makes games run faster
window.tracer(0)

score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .3
ball.dy = -.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLayer 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))

# Functions
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
    
def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)
    
def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)
    
def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)
    
# Keyboard binding
window.listen()
window.onkeypress(pad_a_up, "w")
window.onkeypress(pad_a_down, "s")
window.onkeypress(pad_b_up, "Up")
window.onkeypress(pad_b_down, "Down")

# Main game loop
while True:
    window.update()
    
    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Check for borders
    #Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # For Linux users
        os.system("aplay bump1.wav&")
        # For Mac users
        #os.system("afplay bump1.wav&")
        # For Windows users
        #winsound.PlaySound("bump1.wav", winsound.SND_ASYNC)
    #Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # For Linux users
        os.system("aplay bump1.wav&")
        # For Mac users
        #os.system("afplay bump1.wav&")
        # For Windows users
        #winsound.PlaySound("bump1.wav", winsound.SND_ASYNC)
    #Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PLayer 1: {} Player 2: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    #Left
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PLayer 1: {} Player 2: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

        
    # Paddel ball collision
    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        # For Linux users
        os.system("aplay bump1.wav&")
        # For Mac users
        #os.system("afplay bump1.wav&")
        # For Windows users
        #winsound.PlaySound("bump1.wav", winsound.SND_ASYNC)
    
    elif ball.xcor() > 340 and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        # For Linux users
        os.system("aplay bump1.wav&")
        # For Mac users
        #os.system("afplay bump1.wav&")
        # For Windows users
        #winsound.PlaySound("bump1.wav", winsound.SND_ASYNC)