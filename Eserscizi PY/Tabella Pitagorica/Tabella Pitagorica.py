def make_tabella_pitagorica():
    return[[numero*indice for numero in range(1,11)]for indice in range(1,11)]

def write_file(nomeFile,tabella_pitagoriga):
    f = open(nomeFile,"w")
    for riga in tabella_pitagoriga:
        f.write(f"{riga}\n")
    f.close()

def main():
    tabella_pitagorica = make_tabella_pitagorica()
    print(tabella_pitagorica)
    write_file("tabella_pitagorica",tabella_pitagorica)

if __name__ == "__main__":
      main()