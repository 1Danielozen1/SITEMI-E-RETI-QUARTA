
som = 0
file = open("4AROB_GITA.csv","r")
lista_righe = file.readlines()
file.close()
diz = {"Nome":[], "Euro": []}

for riga in lista_righe[1:]:
    lista =  riga[:-1].split(";")
    #print(lista)
    diz["Nome"] = lista[1]
    diz["Euro"] = lista[2]
    print(diz["Nome"],diz["Euro"])
cogn = input("Inserisci il cognome: ")
for a in diz:
    if(cogn == diz["Nome"]):
        print("ok")
        som = som + diz["Euro"]
    else:
        pass
print(som)
