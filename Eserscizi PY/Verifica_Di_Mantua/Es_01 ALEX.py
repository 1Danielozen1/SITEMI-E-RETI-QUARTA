from re import T
import turtle


class barcode():
    def __init__(self, stringa):
        self.byte="00000000"
        self.stringa=stringa
        self.string_int=None
        self.string_bin=None

    def alfBin(self):
        self.string_int=""
        for element in self.stringa:
            self.string_int=self.string_int+str(ord(element))

        """
        for number in self.string_int:
            
            for element in self.byte:
                
                if(element == "0" and number  == "0"):             #versione scartata del metodo seguente
                   temp = temp + '0'
                else:
                   temp = temp + '1'
        """
        lista_grupp = [int(Bin)for Bin in self.string_int]
        self.string_bin = ""                                    #cerca di fare in modo che ogni elemento di string_bin abbia 8 bit
        for gruppo in lista_grupp:
            temp= bin(gruppo)[2:]
            temp = "0"*(8-len(temp))+temp
            self.string_bin = self.string_bin+temp
        
        return(self.string_bin)
 

    def stampa(self):
        finesta = turtle.screensize(100, 100) #regola dimensionéfinestra
        posx=-(64*4)
        bar=turtle.Turtle()
        bar.speed(0)
        bar.width(4)
        bar.setpos(posx, 0)
        bar.setheading(270) #imposta la direzione del turtle
        for bit in self.string_bin:
            if (bit=='0'):         #controlla se il bit è 0 o 1 e decide il colore della riga
                bar.color("white")
            else:
                bar.color("black")
            bar.penup()
            bar.setpos(posx, 0) #muove il turtle in posizione per la prossima riga
            bar.pendown()
            bar.forward(100)
            posx=posx+5
        turtle.done()
            
            

def main():
    barra=barcode("A73RO0IC")
    print(barra.alfBin()) #richiama la funzione e controlla e print output per il debug
    barra.stampa()

if __name__=="__main__":
    main()