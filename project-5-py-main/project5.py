import turtle


my_turtle = turtle.Turtle()
pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("pink")

pen.color("yellow")
pen.begin_fill()

for _ in range(6):
    my_turtle.forward(100)
    my_turtle.left(60)


pen.end_fill()


screen.mainloop()