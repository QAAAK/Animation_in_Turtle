import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed('fastest')
for x in range(200):
    t.pencolor('blue')
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(79)
