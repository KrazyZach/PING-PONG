import turtle as t
import random as r
screen = t.Screen()
screen.bgcolor("Black")

width = screen.window_width()
height = screen.window_height()
side_of_height = (height / 2)
side_of_width = (width / 2)
screen.tracer(0)  
screen.listen()

def board(): 
    def setup():
        setup = t.Turtle()
        setup.hideturtle()
        setup.speed(0)
        setup.color("White")
        setup.left(90)
        setup.pensize(8)
        setup.penup()
        setup.goto(0, -side_of_height)
        y = -side_of_height
        while y <= side_of_height:
            setup.pendown()  
            setup.forward(10)
            setup.penup()  
            setup.forward(30)
            y = setup.ycor()  
    setup()

paddle = t.Turtle()
paddle2 = t.Turtle()
paddle.penup()
paddle.color("white")
paddle.shape("square")
paddle2.penup()
paddle2.color("white")
paddle2.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle2.shapesize(stretch_wid=1, stretch_len=5)
paddle.goto(390 , 0)
paddle.left(90)
paddle2.goto(-390 , 0)
paddle2.left(90)
def paddle_forward():
    paddle.forward(30)
    screen.update()
def paddle_down():
    paddle.backward(30)
    screen.update()
screen.onkeypress(paddle_forward, "Up")
screen.onkeypress(paddle_down, "Down")
def paddle_forward2():
    paddle2.forward(30)
    screen.update()
def paddle_down2():
    paddle2.backward(30)
    screen.update()
screen.onkeypress(paddle_forward2, "w")
screen.onkeypress(paddle_down2, "s")

board()


ball = t.Turtle()
ball.color("White")
ball.penup()
ball.shape("circle")
tolarence = 53
tolarence2 = 10
ball.setheading(r.randint(0,75))
joke = ball.heading()

score1 = 0
score2 = 0
def score():
    screen.update()
    global score4, score3
    score3 = t.Turtle()
    score4 = t.Turtle()
    score3.color("White")
    score3.hideturtle()
    score3.penup()
    score3.goto(100, 300)
    score3.write(score1, move=False, align='right', font=('Arial', 30, 'normal'))
    score4.hideturtle()
    score4.penup()
    score4.color("White")
    score4.goto(-100, 300)
    score4.write(score2, move=False, align='right', font=('Arial', 30, 'normal'))


x = True
def move_ball():
    def reset_ball():
        ball.goto(0,0)
        ball.setheading(r.randint(0, 150))

    global score1, score2, x
    ball.speed(10.5)
    ball.forward(10)
    screen.update()
    if abs(paddle.xcor() - ball.xcor()) <= tolarence2 and abs(paddle.ycor() - ball.ycor()) <= tolarence:
        ball.setheading(180 - ball.heading())
    elif abs(paddle2.xcor() - ball.xcor()) <= tolarence2 and abs(paddle2.ycor() - ball.ycor()) <= tolarence:
        ball.setheading(180 - ball.heading())
    elif abs(ball.xcor()) >= 420:
        if ball.xcor() >= 420:
            score2 += 1 
            score3.clear()
            score4.clear()
            score()               
        else:
            score1 += 1
            score4.clear()
            score3.clear()
            score()
        if score1 == 5 or score2 == 5:
            screen.clear()
            screen.bgcolor("Black")
            score4.goto(0,0)
            if score1 == 5:
                score4.write("GAME OVER, RIGHT PLAYER WINS", move=False, align='center', font=('Arial', 30, 'normal'))
            else:
                score4.write("GAME OVER, LEFT PLAYER WINS", move=False, align='center', font=('Arial', 30, 'normal'))
            x = False
        else:
            reset_ball()
                      
    elif abs(ball.ycor()) >= side_of_height:
        ball.setheading(360 - ball.heading())
    elif  abs(side_of_height - ball.ycor()) <= tolarence and abs(side_of_width - ball.xcor()) <= tolarence2:
        ball.setheading(180 - ball.heading())

    if x:
        screen.ontimer(move_ball, 20)

print(joke)
screen.update()
score()
screen.ontimer(move_ball, 3000)
screen.exitonclick()
