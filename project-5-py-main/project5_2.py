import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("pink")
turtle.showturtle()
turtle.shape("turtle")
length1 = 100
length2 = 200
angle = 90
turtle.forward(length1)
turtle.right(angle)
turtle.forward(length2)
turtle.right(angle)
turtle.forward(length1)
turtle.right(angle)
turtle.forward(length2)
turtle.right(angle)
screen.mainloop()