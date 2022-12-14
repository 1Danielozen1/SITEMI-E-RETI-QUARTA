def leggiFile(nomeFile):
    """La funzione legge il file dei matematici"""
    file = open(nomeFile,"r")
    lista_righe = file.readlines() #legge il file e ritorna le righe del file.
    file.close()

    diz_matematici = {"id":[],"nomi":[]} #id sono numeri, mentri i nomi sono str

    for riga in lista_righe[1:]:
        lista_campi =  riga[:-1].split(", ")
        id = int(lista_campi[0])
        nome = lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome)

    return diz_matematici

def nomeID(id,diz_matematici):
    listaId = diz_matematici["id"]
    listanomi= diz_matematici["nomi"]
    for a,b in zip(listaId,listanomi):
        if a == id:
            return b



def main():
    nomefile = input("Inserisci il nome del file: ")
    id = 0
    while id >= 4 or id <= 0:
        id = int(input("Inserisci l'ID: "))
    diz_matematici = leggiFile(nomefile)
    print(diz_matematici)
    nome = nomeID(id,diz_matematici)
    print(nome)

if __name__ == "__main__":
    main()