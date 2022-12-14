
def leggiFile():
    file = open("./covid-19_gen1.txt","r")
    lista_righe = file.readlines()
    file.close()

    s = ""
    for a in lista_righe:
        s = s+a[:-1]
    #print(s)
    return s

def trovaOcc(f,diz_lett):
    l = [0,0,0,0]
    for a in f:
        #print(a)
        if diz_lett[0] == a:
            l[0]+1
        elif diz_lett[1] == a:
            l[1]+1
        elif diz_lett[2] == a:
            l[2]+1
        elif diz_lett[3] == a:
            l[3]+1
    return l



def main():
    f = leggiFile()
    diz_lett = ["A","C","G","T"]
    print(trovaOcc(f,diz_lett))

if __name__ == "__main__":
    main()