from turtle import *

# 爱心
# def curvemove():
# 	for i in range(200):
# 		right(1)
# 		fd(1)

# pensize(1)
# speed(1)
# color('red','red')
# begin_fill()
# left(140)
# fd(111.65)
# curvemove()
# left(120)
# curvemove()
# fd(111.65)
# end_fill()

# begin_fill()
# setx(20)
# sety(20)
# color('green','green')
# begin_fill()
# left(280)
# fd(111.65)
# curvemove()
# left(120)
# curvemove()
# fd(111.65)
# end_fill()

# hideturtle()
# done()

#玫瑰花

def DegreeCurve(n,r,d=1):
	for i in range(n):
		left(d)
		circle(r,abs(d))

# 初始位置设定
s = 0.2 # size
setup(450*5*s, 750*5*s)
pencolor("black")
fillcolor("red")
speed(100)
penup()
goto(0, 900*s)
pendown()
# 绘制花朵形状
begin_fill()
circle(200*s,30)
DegreeCurve(60, 50*s)
circle(200*s,30)
DegreeCurve(4, 100*s)
circle(200*s,50)
DegreeCurve(50, 50*s)
circle(350*s,65)
DegreeCurve(40, 70*s)
circle(150*s,50)
DegreeCurve(20, 50*s, -1)
circle(400*s,60)
DegreeCurve(18, 50*s)
fd(250*s)
right(150)
circle(-500*s,12)
left(140)
circle(550*s,110)
left(27)
circle(650*s,100)
left(130)
circle(-300*s,20)
right(123)
circle(220*s,57)
end_fill()
# 绘制花枝形状
left(120)
fd(280*s)
left(115)
circle(300*s,33)
left(180)
circle(-300*s,33)
DegreeCurve(70, 225*s, -1)
circle(350*s,104)
left(90)
circle(200*s,105)
circle(-500*s,63)
penup()
goto(170*s,-30*s)
pendown()
left(160)
DegreeCurve(20, 2500*s)
DegreeCurve(220, 250*s, -1)
# 绘制一个绿色叶子
fillcolor('green')
penup()
goto(670*s,-180*s)
pendown()
right(140)
begin_fill()
circle(300*s,120)
left(60)
circle(300*s,120)
end_fill()
penup()
goto(180*s,-550*s)
pendown()
right(85)
circle(600*s,40)
# 绘制另一个绿色叶子
penup()
goto(-150*s,-1000*s)
pendown()
begin_fill()
rt(120)
circle(300*s,115)
left(75)
circle(300*s,100)
end_fill()
penup()
goto(430*s,-1070*s)
pendown()
right(30)
circle(-600*s,35)
done()