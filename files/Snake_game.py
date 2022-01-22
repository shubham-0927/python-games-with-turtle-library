import turtle
import time
import random
delay=0.1

scr = turtle.Screen()
scr.title("Snake game")
scr.bgcolor("black")
scr.setup(width=600, height=600)
scr.tracer(0)

brd=turtle.Turtle()
brd.penup()
brd.setposition(-300,-300)
brd.color("white")
brd.pendown()
brd.pensize(4)
for j in range(4):
    brd.forward(600)
    brd.left(90)
brd.hideturtle()

#for head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "right"


#for food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)

segments=[]
#for score
pen=turtle.Turtle()
pen.speed()
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center",font=('Arial',24,'normal'))


def up():
    if head.direction !="down":
        head.direction="up"
def down():
    if head.direction !="up":
        head.direction="down"
def left():
    if head.direction != "right":
        head.direction="left"
def right():
    if head.direction != "left":
        head.direction="right"
def forexit():
    scr.bye()

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
scr.listen()
scr.onkeypress(up,"w")
scr.onkeypress(down,"s")
scr.onkeypress(left,"a")
scr.onkeypress(right,"d")
scr.onkeypress(forexit,"x")

while True:
    scr.update()
    score = len(segments)
    pen.clear()
    pen.write("            SCORE: {}             ".format(score), align='center', font=('Arial', 20))
    pen.write("                                                x = exit key", font=('Arial', 12))

    if head.xcor() > 290 or -290 > head.xcor() or head.ycor()> 290 or (-290)> head.ycor():
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for s in segments:
            s.goto(1000,1000)

        segments.clear()

    if head.distance(food)<20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)

    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y= segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments)>0:
        x= head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    for s in segments:
        if s.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction =" stop"
            for s in segments:
                s.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)
scr.mainloop()