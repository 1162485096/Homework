import turtle
import math
turtle.pensize(1)
turtle.up()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(300)
turtle.down()
turtle.color("red")
turtle.begin_fill()
for i in range(2):
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(600)
turtle.end_fill()
turtle.up()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
turtle.down()
# 大五角星
turtle.color("yellow")
turtle.right(162)
def paint1():
    turtle.begin_fill()
    l=(60*math.cos(math.radians(18)))/(1+math.sin(math.radians(18)))
    for i in range(5):
        turtle.forward(l)
        turtle.left(72)
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()
paint1()
#画五角星
def paint2():
    turtle.right(162)
    turtle.begin_fill()
    l=(20*math.cos(math.radians(18)))/(1+math.sin(math.radians(18)))
    for i in range(5):
        turtle.forward(l)
        turtle.left(72)
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()
    
def paint3():
    turtle.right(72)
    turtle.begin_fill()
    l=(20*math.cos(math.radians(18)))/(1+math.sin(math.radians(18)))
    for i in range(5):
        turtle.forward(l)
        turtle.left(72)
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()
 
def paint4():
    turtle.left(18)
    turtle.begin_fill()
    l=(20*math.cos(math.radians(18)))/(1+math.sin(math.radians(18)))
    for i in range(5):
        turtle.forward(l)
        turtle.left(72)
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()
    
#第一个小五角星
turtle.up()
turtle.left(72)
turtle.forward(120)
turtle.down()
paint2()
#第二个小五角星
turtle.up()
turtle.left(162)
turtle.forward(20)
turtle.right(90)
turtle.forward(40)
turtle.right(math.degrees(math.atan(1/7)))
turtle.forward(20)
turtle.down()
paint2()
#第三个小五角星
turtle.up()
turtle.left(180-math.degrees(math.atan(1/7)))
turtle.forward(20)
turtle.left(90)
turtle.forward(20*(1/7))
turtle.down()
paint3()
#第四个小五角星
turtle.up()
turtle.right(18)
turtle.forward(60)
turtle.right(90)
turtle.forward(20)
turtle.down()
paint4()
turtle.color("red")



