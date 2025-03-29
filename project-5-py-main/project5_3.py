import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.bgcolor("pink")
for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)

turtle.done()


screen.mainloop()