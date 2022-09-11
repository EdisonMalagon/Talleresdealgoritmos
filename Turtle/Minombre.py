import turtle

t = turtle.Turtle()

t.speed(10)
t.pensize(6)
t.color("red")
t.shape("circle")

t.bk(100)
t.rt(90)
t.fd(90)
t.lt(90)
t.fd(90)
t.lt(180)
t.fd(90)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(90)

t.up()
t.goto(20,0)
t.down()

t.color("yellow")
t.fd(120)
t.rt(90)
t.fd(180)
t.rt(90)
t.fd(120)
t.rt(180)
t.fd(30)
t.lt(90)
t.fd(180)

t.up()
t.goto(160,0)
t.down()

t.color("blue")
t.fd(-180)


t.up()
t.goto(20,0)
t.down()

t.color("green")
for i in range(20):
    t.forward(i * 10)
    t.right(144)
    
turtle.done()