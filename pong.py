import turtle
import winsound

win = turtle.Screen()
win.title('pong by Hulgesh')
win.bgcolor("black")
win.setup(height = 600 ,width = 800)



#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Player A:0  Player B:0",align="center",font=("Courier",20,"normal"))

#Ball
ball = turtle.Turtle()
ball.color ("white")
ball.speed(2.0)
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Paddle A  
paddle_a = turtle.Turtle()
paddle_a.color ("white")
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len = 1,stretch_wid = 5)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.color ("white")
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len = 1,stretch_wid = 5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Score
score_a = 0
score_b = 0


# Function

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



# keybord binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")  
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down") 

# Main loop

while True:
    win.update()
    
    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
    
    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",20,"normal"))


    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",20,"normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() >paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() >paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    