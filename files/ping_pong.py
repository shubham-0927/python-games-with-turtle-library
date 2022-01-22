import turtle as t


playerAscore=0
playerBscore=0
window=t.Screen()
window.title("pong game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(100000)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=0.5)
leftpaddle.penup()
leftpaddle.goto(-350,0)


#creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=0.5)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ballxdirection=0.2
ballydirection=0.2


#creating pen for scorecard
pen=t.Turtle()
pen.speed()
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center",font=('Arial',24,'normal'))


def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)


def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)


def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)


def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

def forexit():
    window.bye()

#keys

window.listen()
window.onkeypress(leftpaddleup,"w")
window.onkeypress(leftpaddledown,"s")
window.onkeypress(rightpaddleup,"Up")
window.onkeypress(rightpaddledown,"Down")
window.onkeypress(forexit,"x")

while True:
    window.update()

    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor() - ballydirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection= ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection= ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection= ballxdirection
        playerAscore=playerAscore +1
        pen.clear()
        pen.write("player A:{}                                 player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial'))
        pen.write("                                                x = exit key", font=('Arial', 12))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection= ballxdirection
        playerBscore=playerBscore +1
        pen.clear()
        pen.write("player A:{}                                 player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial'))
        pen.write("                                                x = exit key", font=('Arial', 12))
    #collision

    if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+45 and ball.ycor()>rightpaddle.ycor() - 45):
        ball.setx(340)
        ballxdirection=ballxdirection*-1


    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 45 and ball.ycor() > leftpaddle.ycor() - 45):
        ball.setx(-340)
        ballxdirection = ballxdirection*-1

