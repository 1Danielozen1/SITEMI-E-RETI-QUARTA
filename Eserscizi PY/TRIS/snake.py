#Usando il metodo onkey() di turtle implementare una versione minimale del gioco snake in Python. Fare uso delle classi. 
import turtle
import time

def destra():
    turtle.right(90)
def avanti():
    turtle.fd(1)  
def sinistra():
    turtle.left(90)

def main():
    screen = turtle.screensize(120,120,"black")
    turtle.color("lime")
    turtle.listen()
    turtle.onkeypress(destra,"d")
    turtle.onkeypress(sinistra,"a")
    while True:    
        avanti()

    turtle.done()


if __name__=="__main__":
    main()