import turtle
import colorsys
t = turtle.Turtle()
turtle.title("FIRST GAME")
turtle.Screen().bgcolor("orange")
t.fillcolor("black")
t.shape("square")
t.pensize(5)
t.speed(15)
n = 50
h = 2
for i in range(40):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+1/n
    t.pencolor(c)
    for j in range(4):
        t.forward(i)
        t.right(10)
        t.left(10)
        t.forward(i)
    t.right(120)


t.write("FIRST GAME", font=("Arial", 20, "normal"))





turtle.done()

