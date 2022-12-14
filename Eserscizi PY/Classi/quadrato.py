class Quadrato:
    def __init__(self,x,y,lato):
        self.x = x
        self.y = y
        self.lato = lato
    def perimetro(self):
        return(self.lato*4)
    def area(self):
        return(self.lato**2)
    def isdentro(self,xp,yp):
        if(self.x <= xp and self.x+self.lato >= xp and self.y <= yp and self.y+self.lato >= yp):
            print("Interno")
        else:
            print("esterno")

def main():
    quadrato = Quadrato(11,15,5)
    print(quadrato.perimetro())
    print(quadrato.area())
    quadrato.isdentro(12,16)

if __name__ == "__main__":
    main()