import turtle as t
import math
t.colormode(255)
rcblue=(4,0,174)
rcred=(254,0,0)

def ol(r,n):
    na = 15 / 180 * math.pi
    ol=2*r*math.cos(na)
    ol=int(round(ol))
    return ol

def loop(r,n):
    t.fd(ol(r,n))
    t.right(150)

def main0(a,b):  #沒有循環和復雜角度操作的時候用goto比較快
    t.color(rcred)
    t.penup()
    t.goto(-a/2,b/2)
    t.pendown()
    t.begin_fill()
    t.goto(-a/2,-b/2)
    t.goto(a/2,-b/2)
    t.goto(a/2,b/2)
    t.end_fill()
    t.penup()
    t.goto(-a/4,b/4)
    t.pendown()

def main1(a1,b1):
    t.color('gray',rcblue)
    t.penup()
    t.right(90)
    t.fd(b1/2)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.fd(a1/2)
    t.left(90)
    t.fd(b1)
    t.left(90)
    t.fd(a1)
    t.left(90)
    t.fd(b1)
    t.left(90)
    t.fd(a1/2)
    t.end_fill()
    t.penup()
    t.goto(-a/4,b/4)
    t.seth(0)
    t.pendown()

def main2(r,n):
    t.pensize = 20
    t.color('white', 'white')
    t.penup()
    t.fd(r)
    t.right(180 - 30 / 2)
    t.pendown()
    t.begin_fill()
    for i in range(12):
        loop(r,n)
    t.end_fill()
    t.penup()
    t.goto(-a/4,b/4)
    t.seth(0)
    t.pendown()

def main3(r1,r2):
    t.color(rcblue, rcblue)  # t.color(),not t.pencolor()
    t.begin_fill()
    t.up()
    t.right(90)
    t.fd(r1)
    t.left(90)
    t.pd()
    t.circle(r1)
    t.end_fill()
    t.penup()
    t.goto(-a/4,b/4)
    t.pendown()
    t.color('white', 'white')
    t.begin_fill()
    t.pu()
    t.right(90)
    t.fd(r2)
    t.left(90)
    t.pd()
    t.circle(r2)
    t.end_fill()
    t.penup()
    t.goto(-a/4,b/4)
    t.seth(0)
    t.pendown()

def main(a,b):
    a1 = a / 2
    b1 = b / 2
    r = a1 / 4
    n = 8
    r2 = a1 / 8
    r1 = b1 * 17 / 80
    main0(a,b)
    main1(a1,b1)
    main2(r,n)
    main3(r1,r2)

a=1020
b=680
t.setup(1100,700,100,0)
main(a,b)
t.done()
