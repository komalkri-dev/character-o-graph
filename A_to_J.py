import turtle

def draw_A(offset):
    a = turtle.Turtle()
    a.speed(4)
    a.color("yellow")
    a.up()
    a.forward(offset)
    a.down()

    a.left(73.5)
    a.forward(72.1)
    a.right(147)
    a.forward(72.1)
    a.backward(28)
    a.right(106.5)
    a.forward(25.9)
    a.hideturtle()

def draw_B(offset):
    # draw b shape
    b = turtle.Turtle()
    b.speed(4)
    b.color("pink")
    b.up()
    b.forward(offset)
    b.down()

    b.left(90)
    b.forward(70)
    b.right(90)
    b.forward(15)
    for ba in range(18):
        b.forward(3.15)
        b.right(10)
    b.forward(17)
    b.right(180)
    b.forward(17)
    for ba in range(18):
        b.forward(3.10)
        b.right(10)
    b.forward(22)

    b.hideturtle()


def draw_C(offset):
    # drawing alphabet c
    c = turtle.Turtle()
    c.speed(4)
    c.color("cyan")
    c.up()
    c.forward(offset)
    c.down()

    c.left(90)
    c.up()
    c.forward(70)
    c.right(90)
    c.forward(42)
    c.right(180)
    # drawing starts here
    c.down()
    c.forward(11.5)
    for ca in range(9):
        c.forward(4.9)
        c.left(10)
    c.forward(14)
    for ca in range(9):
        c.forward(4.9)
        c.left(10)
    c.forward(15.4)

    c.hideturtle()


def draw_D(offset):
    # drawing alphabet d
    d = turtle.Turtle()
    d.speed(4)
    d.color("white")
    d.up()
    d.forward(offset)
    d.down()

    d.left(90)
    d.forward(70)
    d.right(90)
    d.forward(11.5)
    for da in range(9):
        d.forward(4.9)
        d.right(10)
    d.forward(13.9)
    for da in range(9):
        d.forward(5.04)
        d.right(10)
    d.forward(15.4)

    d.hideturtle()


def draw_E(offset):
    # drawing alphabet e
    e = turtle.Turtle()
    e.speed(4)
    e.color("orange")
    e.up()
    e.forward(offset)
    e.down()

    e.left(90)
    e.forward(70      )
    e.right(90)
    e.forward(38.5)
    e.backward(38.5)
    e.right(90)
    e.forward(35)
    e.left(90)
    e.forward(31.5)
    e.backward(31.5)
    e.right(90)
    e.forward(35)
    e.left(90)
    e.forward(42)

    e.hideturtle()


def draw_F(offset):
    # drawing alphabet f
    f = turtle.Turtle()
    f.speed(4)
    f.color("lime")
    f.up()
    f.forward(offset)
    f.down()

    f.left(90)
    f.forward(70)
    f.right(90)
    f.forward(42)
    f.backward(42)
    f.right(90)
    f.forward(35)
    f.left(90)
    f.forward(35)

    f.hideturtle()


def draw_G(offset):
    g = turtle.Turtle()
    g.speed(9)
    g.color('pink')
    g.up()
    g.forward(offset)
    g.down()

    g.up()
    g.left(90)
    g.forward(70)
    g.right(90)
    g.forward(39.2)
    g.right(90)
    g.forward(3.5)
    g.right(180)
    g.down()
    # start
    g.left(40)
    for ga in range(5):
        g.forward(1.4)
        g.left(10)
    g.forward(14)
    for ga in range(9):
        g.forward(3.01)
        g.left(10)

    g.forward(35)

    for ga in range(9):
        g.forward(2.94)
        g.left(10)

    g.forward(7.7)

    for ga in range(9):
        g.forward(2.94)
        g.left(10)

    g.forward(17.5)
    g.left(90)
    g.forward(17.5)

    g.hideturtle()


def draw_H(offset):
    # drawing alphabet h
    h = turtle.Turtle()
    h.speed(4)
    h.color("cyan")
    h.up()
    h.forward(offset)
    h.down()

    h.left(90)
    h.forward(70)
    h.backward(35)
    h.right(90)
    h.forward(42)
    h.left(90)
    h.forward(35)
    h.backward(70)

    h.hideturtle()


def draw_I(offset):
    # drawing alphabet i
    i = turtle.Turtle()
    i.speed(4)
    i.color("yellow")
    i.up()
    i.forward(offset)
    i.forward(3.5)
    i.down()

    i.left(90)
    i.forward(70)
    i.hideturtle()


def draw_J(offset):
    # drawing alphabet j
    j = turtle.Turtle()
    j.speed(4)
    j.color("white")

    j.up()
    j.forward(offset)
    j.left(90)

    j.forward(70)
    j.right(90)
    j.forward(42)
    j.down()

    j.right(90)
    j.forward(47.6)
    for ja in range(18):
        j.forward(3.64)
        j.right(10)
    j.forward(7)
    j.hideturtle()
   

