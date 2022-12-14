"""
S = "chikakok"
print(S[::2])


n = int(input("Inserisci il numero: "))
lista = [1]*n
lista[0],lista[-1]= 0,0
print(lista)


METODO LENTO:
n = int(input("Inserisci il numero: "))
l=[]

for i in range(1,n+1):
    l.append(i)
    
print(l)
"""
#METODO VELOCE:
n = int(input("Inserisci il numero: "))
l = [i for i in range(1,n+1)]
print(l)