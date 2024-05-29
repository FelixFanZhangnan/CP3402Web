import turtle

wn = turtle.Screen()
wn.title("Pong by Zhangnan Fan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # ball move 2 px every time
ball.dy = -2

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("red")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = -2 # ball move 2 px every time
ball1.dy = 2


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#Function

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


# Keybord binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

def ball_move(ball_name):
    if (ball_name.xcor() > 340 and ball_name.xcor() < 350) and (ball_name.ycor() < paddle_b.ycor() + 40 and ball_name.ycor() > paddle_b.ycor() - 40):
        ball_name.setx(340)
        ball_name.dx *= -1

    if (ball_name.xcor() < -340 and ball_name.xcor() > -350) and (ball_name.ycor() < paddle_a.ycor() + 40 and ball_name.ycor() > paddle_a.ycor() - 40):
        ball_name.setx(-340)
        ball_name.dx *= -1

def ball_action(ball_name):
    ball_name.setx(ball_name.xcor() + ball_name.dx)
    ball_name.sety(ball_name.ycor() + ball_name.dy)

def border_checking(ball_name, score_1, score_2):
    if ball_name.ycor() > 290:
        ball_name.sety(290)
        ball_name.dy *= -1

    if ball_name.ycor() < -290:
        ball_name.sety(-290)
        ball_name.dy *= -1

    if ball_name.xcor() > 390:
        ball_name.goto(0,0)
        ball_name.dx *= -1
        score_1 += 1
        
    # pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

    if ball_name.xcor() < -390:
        ball_name.goto(0,0)
        ball_name.dx *= -1
        score_2 += 1

    # pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))
    return score_1, score_2

    




# Main game loop
while True:
    wn.update()
    # Move the ball
    ball_action(ball)
    ball_action(ball1)
    
    #Border checking
    score_a, score_b = border_checking(ball,score_a, score_b) 
    pen.clear()
    
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

    score_a, score_b = border_checking(ball1,score_a, score_b)
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))
    
    # paddle and ball collicision
    ball_move(ball)
    ball_move(ball1)
    
