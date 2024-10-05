import turtle 

turtle.setup(600,600)
turtle.speed(0)
turtle.color("red")
turtle.width(100)
turtle.begin_fill()
turtle.end_fill()
turtle.goto(0,0)

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
    
turtle.done()