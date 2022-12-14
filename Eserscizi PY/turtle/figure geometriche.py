import turtle
import math
"""
def triangolo(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-400,390)
    curs.pendown()
    curs.right(angolo)
    curs.forward(120)
    for _ in range(1,lato):
        curs.right(angolo*2)
        curs.forward(120)
    curs.color("red")
    curs.end_fill()

def quadrato(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-300,390)
    curs.pendown()
    for _ in range(lato):
        curs.right(angolo)
        curs.forward(100)
    curs.color("orange")
    curs.end_fill()

def pentagono(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-110,390)
    curs.pendown()
    for _ in range(0,lato):
        curs.right(angolo)
        curs.forward(65)
    curs.color("yellow")
    curs.end_fill()

def esagono(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-370,270)
    curs.pendown()
    for _ in range(0,lato):
        curs.right(angolo)
        curs.forward(58)
    curs.color("green")
    curs.end_fill()

def eptagono(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-200,260)
    curs.pendown()
    for _ in range(0,lato):
        curs.right(angolo)
        curs.forward(360/7)
    curs.color("pink")
    curs.end_fill()

def ottagono(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-85,275)
    curs.pendown()
    for _ in range(0,lato):
        curs.right(angolo)
        curs.forward(45)
    curs.color("purple")
    curs.end_fill()

def nonagono(curs,lato,angolo):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(-265,50)
    curs.pendown()
    for _ in range(lato):
        curs.right(angolo)
        curs.forward(40)
    curs.color("blue")
    curs.end_fill()
"""
def poligono(posx,posy,nLati,curs,colore):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(posx,posy)
    curs.pendown()
    angolo = 360/nLati
    lato = 2*60*math.sin(angolo/2*3.1415/180)
    for _ in range(0,nLati):
        curs.right(angolo)
        curs.forward(lato)
    curs.color(colore)
    curs.end_fill()

def main():
    diz_pos={3:(-350,390,"red"),4:(-240,390,"orange"),5:(-110,400,"yellow"),
            6:(-370,270,"pink"),7:(-240,270,"green"),8:(-100,275,"blue"),9:(-370,140,"purple"),10:(-240,140,"lime"),11:(-110,140,"violet")}
    curs = turtle.Turtle()
    finesta = turtle.Screen()
    curs.speed(0)
    for nLati,dati in diz_pos.items():
        poligono(dati[0],dati[1],nLati,curs,dati[2])
    turtle.done()
""" 
   lato,angolo = 3,60
    triangolo(curs,lato,angolo)
    curs.left(30)
    lato,angolo = 4,90
    quadrato(curs,lato,angolo)
    lato,angolo = 5,360/5
    curs.right(54)
    pentagono(curs,lato,angolo)
    lato,angolo = 6,360/6
    curs.right(36)
    esagono(curs,lato,angolo)
    lato,angolo = 7,360/7
    curs.right(26)
    eptagono(curs,lato,angolo)
    lato,angolo = 8, 360/8
    curs.left(26)
    ottagono(curs,lato,angolo)
    lato,angolo = 9, 360/9
    curs.right(180)
    nonagono(curs,lato,angolo)
    """


if __name__ == "__main__":
    main()