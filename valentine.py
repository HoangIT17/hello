#Hi everybody.I'm ROBOT_BRAINS.
import turtle
from turtle import*
import time
wn=Screen()
wn.bgcolor("pink")

fl = turtle.Turtle()
fl.hideturtle()


fl.penup()
fl.left(90)
fl.fd(200)
fl.pendown()
fl.right(90)


fl.fillcolor("red")
fl.begin_fill()
fl.circle(10, 180)
fl.circle(25, 110)
fl.left(50)
fl.circle(60, 45)
fl.circle(20, 170)
fl.right(24) 
fl.fd(30)
fl.left(10)
fl.circle(30, 110)
fl.fd(20)
fl.left(40)
fl.circle(90, 70)
fl.circle(30, 150)
fl.right(30)
fl.fd(15)
fl.circle(80,90)
fl.left(15)
fl.fd(45)
fl.right(165)
fl.fd(20)
fl.left(155)
fl.circle(150,80)
fl.left(50)
fl.circle(150,90)
fl.end_fill()

#1
fl.left(150)
fl.circle(-90, 70)
fl.left(20)
fl.circle(70, 105)
fl.setheading(60)
fl.circle(80, 98)
fl.circle(-90, 40)

#2
fl.left(180)
fl.circle(90,40)
fl.circle(-80,98)
fl.setheading(-83)

#*
fl.fd(30)
fl.left(90)
fl.fd(25)
fl.left(45)
fl.fillcolor("green")
fl.begin_fill()
fl.circle(-80,90)
fl.right(90)
fl.circle(-80,90)
fl.end_fill()
fl.right(135)
fl.fd(60)
fl.left(180)
fl.fd(85)
fl.left(90)
fl.fd(80)

#**
fl.right(90)
fl.right(45)
fl.fillcolor("green")
fl.begin_fill()
fl.circle(80,90)
fl.left(90)
fl.circle(80,90)
fl.end_fill()
fl.left(135)
fl.fd(60)
fl.left(180)
fl.fd(60)
fl.right(90)
fl.circle(200,60)


def curve():
    turtle.speed(99999999)
    for t in range(45):
        turtle.right(5)
        turtle.forward(1)
        
def hearts(x,y):
    turtle.speed(99999999)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(25)
    curve()

    turtle.left(160)
    curve()
    turtle.forward(25)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.left(150)
    

text=turtle.Turtle()
    
def write(message, pos, color):
    x,y = pos
    text.hideturtle()
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style=("Arial",50,"italic")
    text.write(message,font=style)

write("HAPPY",(-490,40),"red")
time.sleep(0.5)
write("VALENTINE",(-550,-35),"red")
time.sleep(0.5)
write("DAY",(-460,-100),"red")
time.sleep(0.5)
write("14/2",(-470,-170),"red")


turtle.onscreenclick(hearts,1)

turtle.mainloop()
wn.mainloop()

#THANKS FLLOWING ME

    
    



