def getDim(c):
    t = 0
    for l in c:
        t += l.count('0')
    return t

def main():
    file = open("mat.csv", "r")
    lista_righe = file.readlines()
    file.close()
    lista = []
    n = 0
    map_num = []

    for riga in lista_righe[0:]:
        # linea senza \n
        riga_senza_n = riga[:-1]
        lista_rig = riga_senza_n.split(",")
        print(lista_rig)
        lista.append(lista_rig)
    
    t=getDim(lista_righe)

    print(f"\n")

    for lista_n in lista:
        lista_l = []
        for element in lista_n:
            if element == '0':
                lista_l.append(n)
                n += 1
            else:
                lista_l.append(-1)
        print(lista_l)
        map_num.append(lista_l)
    #print(map_num)
    print(f"\n")
    tabtutto = []
    for i, line in enumerate(map_num):
        for j, c in enumerate(line):
            celleAd = []
            if c == -1:
                continue

            if j != 0 and map_num[i][j-1] != -1:
                celleAd.append(map_num[i][j-1])
            if j != len(line) - 1 and map_num[i][j + 1] != -1:
                celleAd.append(map_num[i][j + 1])
            if i != 0 and map_num[i - 1][j] != -1:
                celleAd.append(map_num[i - 1][j])
            if i != len(map_num) - 1 and map_num[i + 1][j] != -1:
                celleAd.append(map_num[i + 1][j])

            tabtutto.append([1 if k in celleAd else 0 for k in range(t)])
    
    print("matrice di adiacenza:")
    for l in tabtutto:
        print(l)

if __name__ == '__main__':
    main()