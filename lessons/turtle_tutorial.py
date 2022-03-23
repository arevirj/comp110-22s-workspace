from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()
colormode(255)


leo.speed(50)
leo.hideturtle()
leo.pencolor("blue")
leo.fillcolor(101, 19, 199)
leo.penup()
leo.goto(-150, -150)
leo.pendown()

leo.begin_fill()
i: int = 0
while i < 3: 
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob.pencolor(0, 0, 0)

bob.penup()
bob.goto(-150, -150)
bob.pendown()
bob.speed(150)
side_length: float = 300.0

i: int = 0
while(i < 100):
    bob.forward(side_length)
    bob.left(123)
    side_length = side_length * 0.97
    i = i + 1


done()