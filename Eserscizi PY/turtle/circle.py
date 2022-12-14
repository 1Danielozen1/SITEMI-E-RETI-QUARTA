import turtle
import random
finestra = turtle.Screen()

#ogni secondo si muove a caso di 1cm 
def impazzimento(robot,diz_pos):
    for _ in range(0,7200):
        a = random.randrange(4)
        for numero,dati in diz_pos.items():
            if(numero == a):
                b = random.randrange(4)
                if (b == 0):
                    robot.right(-dati[1])
                    robot.forward(dati[0])
                else:
                    robot.right(dati[1])
                    robot.forward(dati[0])


def main():
    robot = turtle.Turtle()
    diz_pos = {0:(5,0),1:(5,180),2:(5,90),3:(5,-90)}
    robot.speed(0)
    random.seed(1)
    impazzimento(robot,diz_pos)
    turtle.done()




if __name__ == "__main__":
    main()