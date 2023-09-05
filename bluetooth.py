import turtle
t = turtle.Turtle()

t.color("blue")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.circle(34,90)
    t.forward(180)
    t.circle(34,90)
t.end_fill()

t.pencolor("white")
t.pensize(15)
t.penup()
t.goto(10,150)
t.pendown()

t.right(40)
t.forward(100)
t.right(100)
t.forward(60)
t.right(130)
t.forward(160)
t.right(130)
t.forward(60)
t.right(100)
t.forward(100)

t.penup()
t.goto(-95,-110)
t.pendown()
t.pencolor("black")
t.write("Bluetooth", font=("Arial",50,"bold"))

turtle.done()
