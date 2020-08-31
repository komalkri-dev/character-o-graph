import turtle

def draw_T(offset):
    # draws alphabet p
    t = turtle.Turtle()
    t.speed(4)
    t.color('pink')
    t.up()
    t.forward(offset)
    t.down()

    t.left(90)
    t.up()
    t.forward(70)
    t.down()
    t.right(90)
    t.forward(42)
    t.backward(21)
    t.right(90)
    t.forward(70)

    t.hideturtle()


def draw_U(offset):
    # draws alphabet p
    u = turtle.Turtle()
    u.speed(4)
    u.color('white')
    u.up()
    u.forward(offset)

    u.right(90)
    u.backward(70)

    u.down()

    # start
    u.forward(52.5)

    # going right
    for ua in range(9):
        u.forward(2.8)
        u.left(10)
    u.forward(9.8)

    # going up
    for ua in range(9):
        u.forward(2.8)
        u.left(10)
    u.forward(56)

    u.hideturtle()


def draw_V(offset):
    # draws alphabet v
    v = turtle.Turtle()
    v.speed(4)
    v.color('cyan')
    v.up()
    v.forward(offset)
    v.down()

    v.left(90)
    v.up()
    v.forward(70)
    v.down()
    v.right(162)
    v.forward(73.5)
    v.left(146)
    v.forward(72.8)

    v.hideturtle()


def draw_W(offset):
    # draws alphabet w
    w = turtle.Turtle()
    w.speed(8)
    w.color('yellow')
    w.up()
    w.forward(offset)
    w.right(90)
    w.backward(70)
    w.down()

    # start
    w.left(14)
    w.forward(72.1)
    # going up
    w.left(152)
    w.forward(72.1)
    # turning back down
    w.right(152)
    w.forward(72.1)
    # going up again
    w.left(152)
    w.forward(72.8)

    w.hideturtle()


def draw_X(offset):
    # draws alphabet x
    x = turtle.Turtle()
    x.speed(4)
    x.color('orange')
    x.up()
    x.forward(offset)
    x.down()

    x.left(59)
    x.forward(81.55)
    x.left(121)
    x.up()
    x.forward(40.6)
    x.down()
    x.left(121)
    x.forward(81.55)

    x.hideturtle()


def draw_Y(offset):
    # draws alphabet y
    y = turtle.Turtle()
    y.speed(4)
    y.color('lime')
    y.up()
    y.forward(offset)
    y.down()

    y.left(90)
    y.up()
    y.forward(69.3)
    y.right(90)
    y.forward(0.7)
    y.down()
    y.right(60)
    y.forward(40.6)
    y.left(120)
    y.forward(40.6)
    y.backward(40.6)
    y.right(150)
    y.forward(35)

    y.hideturtle()


def draw_Z(offset):
    # drawing alphabet z
    z = turtle.Turtle()
    z.speed(8)
    z.color("yellow")
    z.up()
    z.forward(offset)
    z.down()

    z.up()
    z.left(90)
    z.forward(70)
    z.right(90)
    z.down()
    # drawing starts
    z.forward(40.6)
    z.right(122)
    z.forward(81.9)
    z.left(122)
    z.forward(43.4)

    z.hideturtle()