import tkinter as tk
import turtle

window=tk.Tk()

canvas=tk.Canvas(window,width=600,height=600)
canvas.pack()

screen=turtle.TurtleScreen(canvas)
turtles=screen.turtles()

# If there are existing turtles, use the first one
if turtles:
    turtle = turtles[0]
else:
    # If no turtles exist, create a new one
    turtle = turtle.Turtle()

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.hideturtle()
turtle.exitonclick()
    
window.mainloop()