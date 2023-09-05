import turtle
import colorsys
t = turtle.Turtle()
turtle.title("Introduction")
turtle.Screen().bgcolor("#7FFF00")
t.fillcolor("blue")
t.shape("square")
t.pensize(5)
t.speed(15)
t.pen(pencolor="#32CD32", fillcolor="#32CD32", pensize=10, speed=9)
t.begin_fill()
t.circle(150)
t.end_fill()


c = t.clone()
t.color("green")
c.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()
t.color("#32CD32")
t.begin_fill()
t.circle(80)
t.end_fill()
t.color("#00FF00")
t.begin_fill()
t.circle(60)
t.end_fill()
t.color("#7CFC00")
t.begin_fill()
t.circle(40)
t.end_fill()
t.color("blue")
t.begin_fill()
t.circle(20)
t.end_fill()
t.goto(0,-220)
t.goto(70,-300)
t.goto(0,-220)
t.goto(-70,-300)
t.goto(0,-220)
t.goto(0,-80)
t.goto(-70,-70)
t.goto(0,-80)
t.goto(70,-70)







