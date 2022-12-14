import turtle

class Codice():
    def __init__(self,Ascii):
        self.cod_car = Ascii
        self.cod_bin = None
        self.cod_dec = None
    
    def Ascii2dec(self): #converte il codice dal carattere a decimale
        s = ""
        for a in self.cod_car:
            temp = ord(a)
            #print(temp)
            s = s+str(temp)+"."
        self.cod_dec = s[:-1]
        return self.cod_dec

    def Dec2bin(self): #converte il codice da decimale a binario
        lista_dec=self.cod_dec.split(".")
        lista_grupp = [int(dec)for dec in lista_dec]
        s = ""
        for a in lista_grupp:
            temp= bin(a)[2:]
            temp = "0"*(8-len(temp))+temp
            s = s+str(temp)+"."
        self.cod_bin = s[:-1]
        return self.cod_bin

    def DisegnaCod(self): #disegna il codice a barre
        schermo = turtle.Screen()
        punt = turtle.Turtle()
        punt.pensize(4)
        punt.right(90) #ruoto la turtle di 90 gradi a destra
        punt.hideturtle() #nascondo la turtle
        punt.speed(0)
        x = -(32*4) #inizializzo la posizione x
        y = 100 #inizializzo la posizione y
        lista_bin=self.cod_bin.split(".")
        for a in range(0,len(lista_bin)):
            for b in lista_bin[a]:
                punt.penup()
                punt.setpos(x,y)
                punt.pendown()
                #print(b)
                if b == "0":
                    punt.color("white")
                else:
                    punt.color("black")
                punt.pendown()
                punt.forward(100)
                x = x + 5
                
        turtle.done()


def main():
    codice = "A73RO0IC"
    Cod = Codice(codice)
    print(Cod.Ascii2dec())
    print(Cod.Dec2bin())
    Cod.DisegnaCod()

if __name__ == "__main__":
    main()