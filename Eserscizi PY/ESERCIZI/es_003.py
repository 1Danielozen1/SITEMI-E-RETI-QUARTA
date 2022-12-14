import random

def somma(n1,n2):
    return(n1+n2) 
def sott(n1,n2):
    return (n1-n2)
def molt(n1,n2):
    return(n1*n2)
def div(n1,n2):
    return(n1/n2)

#scelta = int(input("Inserisci l'opzione che preferisci:\n0- Somma\n1- Sottrazione\n2- Moltiplicazione\n3- Divisione\n"))
scelta = random.random(3)
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
l= [somma(n1,n2),sott(n1,n2),molt(n1,n2),div(n1,n2)]
print(f"risultato = {l[scelta]}")

