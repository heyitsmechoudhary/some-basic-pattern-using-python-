import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
t.speed(300)
a = 0
b = 0
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1

    if b==205:
        break
    t.hideturtle()

turtle.done()