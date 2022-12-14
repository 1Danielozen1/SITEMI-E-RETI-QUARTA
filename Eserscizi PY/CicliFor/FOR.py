lista1 = ["a","b","c","d"]
lista2 = [1,2,3,4]

for a in lista1:
    print(a)

print("")

for indice in range(0,len(lista1)):
    print(lista1[indice],end="-")
    print("")
print("")

for b in lista2:
    print(b)
print("")

for elementi in enumerate(lista1):
    print(elementi,end = "")
print("")

for indice,elementi in enumerate(lista1):
    print(elementi,end = "")
print("")


for a,b in zip(lista1,lista2):
    print(a,b)
print("")


#for si lista1C-style
#for con enumerate
#for su lista1 e lista2 C-style (range...)