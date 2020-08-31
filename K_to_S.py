import turtle

def draw_K(offset):
    # drawing alphabet z
    k = turtle.Turtle()
    k.speed(4)
    k.color("cyan")
    k.up()
    k.forward(offset)
    k.down()

    k.left(90)
    k.forward(70)
    k.backward(38.5)
    k.right(45)
    # first leg
    k.forward(54.6)
    k.up()
    k.backward(46.9)
    k.down()
    k.right(89.75)
    # second leg
    k.forward(53.2)

    k.hideturtle()
    


def draw_L(offset):
    # drawing alphabet l
    l = turtle.Turtle()
    l.speed(4)
    l.color("pink")
    l.up()
    l.forward(offset)
    l.down()

    l.left(90)
    l.forward(70)
    l.backward(70)
    l.right(90)
    l.forward(42)

    l.hideturtle()


def draw_M(offset):
    # drawing alphabet m
    m = turtle.Turtle()
    m.speed(4)
    m.color("yellow")
    m.up()
    m.forward(offset)
    m.down()

    m.left(90)
    m.forward(70)
    m.right(150)
    m.forward(56)
    m.left(120)
    m.forward(56)
    m.right(150)
    m.forward(70)

    m.hideturtle()

def draw_O(offset):
    # drawing alphabet o
    o = turtle.Turtle()
    o.speed(8)
    o.color("white")
    o.up()
    o.forward(offset)
    o.down()

    o.left(90)
    o.up()
    o.forward(35.7)
    o.down()
    o.forward(15.4)

    for oa in range(18):
        o.right(10)
        o.forward(3.675)

    o.forward(28)

    for oa in range(18):
        o.right(10)
        o.forward(3.675)

    o.forward(14.7)

    o.hideturtle()


def draw_P(offset):
    # draws alphabet p
    p = turtle.Turtle()
    p.speed(4)
    p.color('cyan')
    p.up()
    p.forward(offset)
    p.down()

    p.left(90)
    p.forward(70)
    p.right(90)
    p.forward(21)
    for pa in range(18):
        p.forward(3.15)
        p.right(10)
    p.forward(23.1)

    p.hideturtle()

def draw_Q(offset):
    # draws alphabet q
    q = turtle.Turtle()
    q.speed(4)
    q.color('yellow')
    q.up()
    q.forward(offset)
    q.down()

    q.left(90)
    q.up()
    q.forward(35.7)
    q.down()
    q.forward(15.4)

    for qa in range(18):
        q.right(10)
        q.forward(3.675)

    q.forward(28)

    for qa in range(18):
        q.right(10)
        q.forward(3.675)

    q.forward(21)

    q.up()
    q.right(180)
    q.forward(24.5)
    q.left(90)
    q.forward(26.6)
    q.down()

    q.right(45)
    q.forward(21)

    q.hideturtle()
  
def draw_R(offset):
    # draws alphabet r
    r = turtle.Turtle()
    r.speed(4)
    r.color('orange')
    r.up()
    r.forward(offset)
    r.down()

    r.left(90)
    r.forward(70)
    r.right(90)

    r.forward(21)
    for ra in range(18):
        r.forward(3.15)
        r.right(10)

    r.forward(24.5)
    r.backward(11.5)

    r.left(132)
    r.forward(45.5)

    r.hideturtle()


def draw_S(offset):
    # draws alphabet s
    s = turtle.Turtle()
    s.speed(4)
    s.color('lime')
    s.up()
    s.forward(offset)
    s.down()

    s.up()
    s.left(90)
    s.forward(70)
    s.right(90)
    s.forward(39.2)
    s.right(90)
    s.forward(3.5)
    s.right(180)
    s.down()

    # start
    s.left(40)
    for sa in range(5):
        s.forward(1.4)
        s.left(10)
    s.forward(20.1)

    # going down
    for sa in range(9):
        s.forward(2.1)
        s.left(10)
    s.forward(11.5)

    # going right
    for sa in range(9):
        s.forward(2.1)
        s.left(10)
    s.forward(18.2)

    # going down again
    for sa in range(9):
        s.forward(2.1)
        s.right(10)
    s.forward(11.2)

    # going left
    for sa in range(9):
        s.forward(2.1)
        s.right(10)
    s.forward(18.2)

    # going up
    for sa in range(9):
        s.forward(2.1)
        s.right(10)

    s.hideturtle()

def draw_N(offset):
    # drawing alphabet n
    n = turtle.Turtle()
    n.speed(8)
    n.color("pink")
    n.up()
    n.forward(offset)
    n.down()

    n.left(90)
    n.forward(70)
    n.right(149)
    n.forward(81.2)
    n.left(149)
    n.forward(70)

    n.hideturtle()
