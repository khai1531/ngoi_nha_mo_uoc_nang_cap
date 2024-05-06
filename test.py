import turtle
import math

t = turtle.Turtle()
t.pensize(1)
t.hideturtle()
t.speed(0)
#Vẽ tầng 1
#-------------------------------#
t.penup()
t.goto(-150, -350)
t.pendown()
t.fillcolor("violet")
t.begin_fill()
t.right(180)
t.forward(600)
t.right(90)
t.forward(50)
t.right(90)
t.forward(600)
t.right(90)
t.forward(50)
t.end_fill()
#-------------------------------#
#Vẽ cầu thang
t.penup()
t.goto(-300, -300)
t.pendown()
t.fillcolor("lightgray")
t.begin_fill()
t.forward(16.66666666666667)
t.right(90)
t.forward( 100)
t.right(90)
t.forward(16.66666666666667)
t.right(90)
t.forward( 100)
t.end_fill()
#-------------------------
t.penup()
t.goto(-275, -316.66666666666667)
t.pendown()
t.fillcolor("lightgray")
t.begin_fill()
t.right(90)
t.forward(16.66666666666667)
t.right(90)
t.forward( 150)
t.right(90)
t.forward(16.66666666666667)
t.right(90)
t.forward( 150)
t.end_fill()
#----
t.penup()
t.goto(-250, -333.33333333333333)
t.pendown()
t.fillcolor("lightgray")
t.begin_fill()
t.right(90)
t.forward(16.66666666666667)
t.right(90)
t.forward( 200)
t.right(90)
t.forward(16.66666666666667)
t.right(90)
t.forward( 200)
t.end_fill()
#-----------------------------#
t.penup()
t.goto(-160, -300)
t.pendown()
t.fillcolor("lightpink")
t.begin_fill()
t.right(180)
t.forward(580)
t.right(90)
t.forward(100)
t.right(90)
t.forward(580)
t.right(90)
t.forward(100)
t.end_fill()
#-------------------------
t.fillcolor("peru")
t.begin_fill()
t.penup()
t.goto(-285, -300)
t.pendown()
t.backward(100)
t.left(90)
t.forward(25)
t.left(90)
t.backward(100)
t.left(90)
t.forward(25)
t.end_fill()
#--------------------
t.fillcolor("peru")
t.begin_fill()
t.penup()
t.goto(-435, -300)
t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.forward(25)
t.left(90)
t.backward(100)
t.left(90)
t.forward(25)
t.end_fill()
#-------------------------#
#Vẽ cửa
t.penup()
t.goto(-325,-300)
t.pendown()
t.fillcolor("peru")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.end_fill()
t.penup()
t.goto(-365,-262.5)
t.pendown()
t.dot(10)
#-----------------------
#Cửa sổ tầng 1
t.fillcolor("lavender")
t.begin_fill()
t.penup()
t.goto(-600, -280)
t.pendown()
t.pensize(5)
t.pencolor("peru")
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.end_fill()
t.penup()
t.goto(-625, -280)
t.pendown()
t.pensize(5)
t.pencolor("peru")
t.left(90)
t.forward(50)
t.penup()
t.goto(-600, -255)
t.pendown()
t.pensize(5)
t.pencolor("peru")
t.left(90)
t.forward(50)
t.penup()
t.goto(-240, -280)
t.pendown()
t.pensize(5)
t.pencolor("peru")
t.fillcolor("lavender")
t.begin_fill()
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.end_fill()
t.penup()
t.goto(-215, -280)
t.pendown()
t.pensize(5)
t.pencolor("peru")
t.backward(50)
t.penup()
t.goto(-240, -255)
t.pendown()
t.pensize(5)
t.pencolor("peru")
t.left(90)
t.forward(50)
t.pencolor("black")
t.pensize(1)
#---------------------------------------#
#Mái tầng 1
t.penup()
t.goto(-150, -200)
t.pendown()
t.fillcolor("lightsalmon")
t.begin_fill()
t.right(180)
t.forward(600)
t.right(90)
t.forward(5)
t.right(90)
t.forward(600)
t.right(90)
t.forward(5)
t.end_fill()
#-------------------------------#
t.penup()
t.goto(-150, -195)
t.pendown()
t.fillcolor("lightsalmon")
t.begin_fill()
t.left(210)
t.forward(100)
t.left(60)
t.forward(500)
t.left(60)
t.forward(100)
t.left(120)
t.forward(600)
t.end_fill()
#--------------------------------
#Tầng 2
t.penup()
t.goto(-200, -108)
t.pendown()
t.fillcolor("lightpink")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(300)
t.right(45)
t.forward(141.4213562373095)
t.left(90)
t.forward(141.4213562373095)
t.left(45)
t.forward(100)
t.end_fill()
#---------------------------
#Cửa sổ tầng 2
t.fillcolor("peru")
t.begin_fill()
t.penup()
t.goto(-630, -68)
t.pendown()
t.left(90)
t.forward(60)
t.left(90)
t.forward(100)
t.circle(30, 180)
t.forward(100)
t.end_fill()
#--------------------------
t.pencolor("peru")
t.fillcolor("lavender")
t.begin_fill()
t.penup()
t.goto(-625,-63)
t.pendown()
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.end_fill()
#---------------------------
t.penup()
t.goto(-600, -63)
t.pendown()
t.pensize(5)
t.backward(80)
#---------------------------
t.penup()
t.goto(-625, -36.33333333333333)
t.pendown()
t.right(90)
t.backward(50)
t.penup()
t.goto(-625,-9.66666666666666)
t.pendown()
t.backward(50)
t.end_fill()
#-----------------------------
t.fillcolor("lavender")
t.begin_fill()
t.penup()
t.goto(-625, 27)
t.pendown()
t.backward(50)
t.penup()
t.goto(-575, 27)
t.pendown()
t.setheading(90)
t.circle(25, 180)
t.end_fill()
#----------------------------
t.fillcolor("lavender")
t.begin_fill()
t.penup()
t.goto(-350,-60)
t.pendown()
t.circle(40)
t.end_fill()
#----------------------------
t.penup()
t.goto(-350,-60)
t.pendown()
t.left(90)
t.forward(80)
t.penup()
t.goto(-310,-20)
t.pendown()
t.left(90)
t.backward(80)
t.pencolor("black")
t.pensize(1)
#----------------------------
#Vẽ mái nhà
t.fillcolor("indianred")
t.begin_fill()
t.penup()
t.goto(-700,-8)
t.pendown()
t.right(225)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(181.4213562373095)
t.right(90)
t.forward(161.4213562373095)
t.left(45)
t.forward(286)
t.right(90)
t.forward(15)
t.right(90)
t.forward(300)
t.right(45)
t.forward(141.4213562373095)
t.left(90)
t.forward(140.4213562373095)
t.end_fill()
#-----------------
t.penup()
t.goto(-560, 80)
t.pendown()
t.fillcolor("lightsalmon")
t.begin_fill()
t.backward(205)
t.left(89)
t.forward(305)
t.pencolor("lightsalmon")
t.goto(-560, 80)
t.forward(105)
t.pencolor("black")
t.penup()
t.goto(-203.17,5.56)
t.pendown()
t.end_fill()
#-----------------------------
#Vẽ mặt trời
position = t.pos()
print(position)
turtle.done()