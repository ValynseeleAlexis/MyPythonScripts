# Valynseele Alexis
# From Learn Python by building Full Course - FreeCodeCamp.org
# 14/01/2020


import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350,0)    
paddleA.shapesize(stretch_wid=5,stretch_len=1)
# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.penup()
paddleB.goto(350,0)    
paddleB.shapesize(stretch_wid=5,stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.deltaX = 0.15
ball.deltaY = 0.15

# Scoring
scoreA = 0
scoreB = 0


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Lolo : " + str(scoreA) +" | Alexis : " + str(scoreB), align="center", font =("Courier",24, "normal"))
# Functions

def paddleA_up():
    y = paddleA.ycor()
    y += 20
    if y < 300:
        paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    if y > -300:
        paddleA.sety(y)

def paddleB_up():        
    y = paddleB.ycor()
    y += 20
    if y < 300:
        paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    if y > -300:
        paddleB.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddleA_up, "z")
window.onkeypress(paddleA_down, "s")
window.onkeypress(paddleB_up, "Up")
window.onkeypress(paddleB_down, "Down")




continuer = True

#Main game loop

while True:
    window.update()
    ball.speed(0.01)

    #Ball mouvements
    ball.setx(ball.xcor() + ball.deltaX)
    ball.sety(ball.ycor() + ball.deltaY)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.deltaY *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.deltaY *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        scoreA += 1
        ball.deltaX *= -1
        pen.clear()
        pen.write("Lolo : " + str(scoreA) +" | Alexis : " + str(scoreB), align="center", font =("Courier",24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        scoreB += 1
        ball.deltaX *= -1
        pen.clear()
        pen.write("Lolo : " + str(scoreA) +" | Alexis : " + str(scoreB), align="center", font =("Courier",24, "normal"))

    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.deltaX *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.deltaX *= -1

  
