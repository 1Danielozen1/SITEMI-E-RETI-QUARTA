import turtle


def testa(stick):
    stick.penup()
    stick.setposition(0,200)
    stick.pendown()
    stick.circle(50)

    #occho sinistro
    stick.color("black")
    stick.begin_fill()
    stick.penup()
    stick.setposition(20,250)
    stick.pendown()
    stick.circle(6)
    stick.end_fill()
    #occhio destro
    stick.begin_fill()
    stick.penup()
    stick.setposition(-20,250)
    stick.pendown()
    stick.circle(6)
    stick.end_fill()

def corpo(stick):
    stick.penup()
    stick.setposition(0,200)
    stick.pendown()
    stick.right(90)
    stick.forward(300)  

def braccia(stick):
    stick.penup()
    stick.setposition(0,150)
    stick.pendown()
    stick.left(90)
    stick.right(45)
    stick.forward(150)
    stick.setposition(0,150)
    stick.right(90)
    stick.forward(150)    


def gambe(stick):
    stick.penup()
    stick.setposition(0,-100)
    stick.pendown()
    stick.left(75)
    stick.forward(200)
    stick.setposition(0,-100)
    stick.right(60)
    stick.forward(200)

def sorriso(stick):

    stick.left(60)
    stick.right(75)
    stick.penup()
    stick.setposition(0,220)
    stick.pendown()
    stick.left(120)
    stick.circle(10,90)
    stick.penup()
    stick.setposition(0,220)
    stick.pendown()
    stick.right(240)
    stick.circle(-10,90)






def main():
    stick = turtle.Turtle()
    finesta = turtle.Screen()
    stick.speed(0)

    testa(stick)
    corpo(stick)
    braccia(stick)
    gambe(stick)
    sorriso(stick)
    stick.penup()
    stick.setposition(100,220)
    stick.pendown()

    turtle.done()




if __name__ == "__main__":
    main()