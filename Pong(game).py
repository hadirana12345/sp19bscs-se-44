import turtle
wn=turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("blue")
wn.setup(width=800,height=600)
wn.tracer(0)
player1score=0
player2score=0

bar1=turtle.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("red")
bar1.shapesize(stretch_wid=5,stretch_len=1)
bar1.penup()
bar1.goto(-350,0)

bar2=turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("green")
bar2.shapesize(stretch_wid=5,stretch_len=1)
bar2.penup()
bar2.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black") 
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = -0.4

score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1  :  0  player 2  :  0",align="center",font=("calibiri",24,"normal"))

def bar1_up():
	y=bar1.ycor()
	if y!=180:
		y+=30
		bar1.sety(y)
def bar1_down():
	y=bar1.ycor()
	if y!=-180:
		y-=30
		bar1.sety(y)
def bar2_up():
	y=bar2.ycor()
	if y!=180:
		y+=30
		bar2.sety(y)
def bar2_down():
	y=bar2.ycor()
	if y!=-180:
		y-=30
		bar2.sety(y)

wn.listen()
wn.onkey(bar1_up,"w")
wn.onkey(bar1_down,"s")
wn.onkey(bar2_up,"Up")
wn.onkey(bar2_down,"Down")
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.dx *= -1
        player1score+=1
        score.clear()
        score.write("player 1  :  {}  player 2  :  {}".format(player1score,player2score),align="center",font=("calibiri",24,"normal"))
    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.dx *= -1
        player2score+=1
        score.clear()
        score.write("player 1  :  {}  player 2  :  {}".format(player1score,player2score),align="center",font=("calibiri",24,"normal"))
    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<bar2.ycor() + 40 and ball.ycor()>bar2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<bar1.ycor() + 40 and ball.ycor()>bar1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1