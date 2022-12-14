import turtle
import random

finestra = turtle.Screen()


def disegnaGriglia(cur):
    posx = -150
    posy = 50
    for _ in range(0,2):
        cur.penup()
        cur.setposition(posx,posy)
        cur.pendown()
        cur.forward(300)
        posy = posy - posy*2
    posx = -50
    posy = 150
    cur.right(90)
    for _ in range(0,2):
        cur.penup()
        cur.setposition(posx,posy)
        cur.pendown()
        cur.forward(300)
        posx = posx - posx*2


def main():
    p1 = input("Inserisci il nome del primo giocatore: ")
    p2 = input("Inserisci il nome del secondo giocatore: ")
    cur = turtle.Turtle() 
    cur.hideturtle()
    dim = 150
    disegnaGriglia(cur)
    diz ={1:(25,25,0,0),2:()}
    l_gioco = [[0,0,0],
               [0,0,0],
               [0,0,0]]

    inizioGioco(cur,p1,p2,l_gioco)

    turtle.done()    

if __name__ == "__main__":
    main()