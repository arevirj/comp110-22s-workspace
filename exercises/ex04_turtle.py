"""This program will incorporate 4 seperate functions to draw unique features of a owl's face. Two distinct eyes, one beak, two ears that will be drawn by one function, and a simple function to draw the head."""

__author__ = "730488173"

from turtle import Turtle, colormode, done
from turtle import tracer, update
colormode(255)


def main() -> None:
    """The entrypoint of my scene. Draws an owl's head by drawing the face first, then both the ears with the same function, a function for each eye, then the beak."""
    tracer(0, 0)
    des: Turtle = Turtle()
    mach: Turtle = Turtle() 
    amp: Turtle = Turtle() 
    sun: Turtle = Turtle()
    vex: Turtle = Turtle()
    face(vex)
    ears(sun, 371.41, 230.00, 105)
    ears(sun, -130.88, 340.00, 165)
    eye1(des, -250.0, 170, 220.0,)
    eye2(mach, 100, 70, 140)
    beak(amp, 25, -90, 120)
    update()
    done()


def turtle_setup(name: Turtle, x: float, y: float) -> None:
    """This function is to setup the position of the turtle to begin a drawing. Is used for several of the other functions."""
    name.hideturtle()
    name.penup()
    name.speed(0)
    name.goto(x, y)
    name.pendown()


def eye1(des: Turtle, x: float, y: float, size: float) -> None:
    """Draws the left eye of the program. A series of 155 degree turns 75 times so that a circular pattern appears, with 'spikes' on the outside and a 'pupil' on the inside."""
    turtle_setup(des, x, y)
    des.fillcolor("black")
    des.pencolor(11, 248, 244)
    des.begin_fill()
    i: int = 0
    while i < 75:
        des.forward(size)
        des.right(155)
        i += 1
    des.forward(size / 2.0)
    des.end_fill()  


def eye2(mach: Turtle, x: float, y: float, size: float) -> None:
    """Draws the right eye of the face. 50 turns at 85 degrees for a widen inner circle, and then slightly decreasing the size so that there is a pattern in the middle. Supposed to be like a rose."""
    turtle_setup(mach, x, y)
    mach.fillcolor("red")
    mach.pencolor("black")
    mach.begin_fill()
    i: int = 0
    while i < 50:
        mach.forward(size)
        mach.left(85)
        i += 1
    mach.end_fill()
    b: int = 0
    while b < 50:
        size *= 0.95
        mach.forward(size)
        mach.left(85)
        b += 1


def beak(amp: Turtle, x: float, y: float, size: float) -> None:
    """Draws the nose of the face. It is a rhombus that draws itself smaller and smaller in the center, giving it a slight 3D illusion."""
    turtle_setup(amp, x, y)
    amp.fillcolor("black")
    amp.pencolor(199, 45, 236)
    amp.setheading(90)
    amp.right(35)
    b: int = 0
    amp.begin_fill()
    while b < 30:
        size *= 0.90
        amp.forward(size)
        amp.left(70)
        amp.forward(size)
        amp.left(110)
        amp.forward(size)
        amp.left(70)
        amp.forward(size)
        amp.left(110)
        b += 1
    amp.end_fill()


def face(vex: Turtle) -> None:
    """Function to draw the face. This should be considered an 'extra' function, with eye1, eye2, nose, and ears being the four required.""" 
    """The face function is straightforward and has specific values for the turtle 'vex', therefore a while loop would have not been helpful."""
    vex.hideturtle()
    vex.speed(0)
    vex.penup()
    vex.goto(25, -200)
    vex.setheading(90)
    vex.pendown()
    vex.fillcolor(230, 230, 230)
    vex.pencolor("black")
    vex.begin_fill()
    vex.right(60)
    vex.forward(400)
    vex.left(60)
    vex.forward(230)
    vex.pos()
    vex.left(60)
    vex.forward(220)
    vex.pos()
    vex.left(45)
    vex.goto(25, 300)
    vex.right(45)
    vex.goto(-130.88, 340.00)
    vex.left(60)
    vex.forward(220)
    vex.left(60)
    vex.forward(230)
    vex.left(60)
    vex.forward(400)
    vex.end_fill()


def ears(sun: Turtle, x: float, y: float, direction: float) -> None:
    """Draws an ear of the owl and creates a repeating white pattern in the middle. can be called for both ears."""
    size: float = 155.46
    turtle_setup(sun, x, y)
    sun.setheading(direction)
    sun.pencolor("white")
    sun.fillcolor("black")
    sun.begin_fill()
    sun.forward(size)
    sun.left(90)
    sun.forward(size)
    sun.left(135)
    sun.forward(size * 1.41)
    sun.end_fill()
    i: int = 0
    while i < 20:
        sun.left(135)
        size *= 0.96
        sun.forward(size)
        sun.left(90)
        sun.forward(size)
        sun.left(135)
        sun.forward(size * 1.41 * 0.96)
        i += 1
        size *= (0.96)


main()


done()