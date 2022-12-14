dizionario = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'z','z':'a',' ': ' '}
messaggio = input("Inserisci il messaggio: ")
criptato = ''
for lettera in messaggio:
    criptato = criptato + dizionario[lettera]

print(f'Il messaggio criptato è {criptato}')

# decodifica al contrario
decod={}
for k,v in dizionario.items():# è un ciclo for fatto simultaneamente su più variabili.
    decod[v]=k
    #print(k,v)
#print(decod)
decrp=""
for lettera in messaggio:
    decrp=(decrp+decod[lettera])

print(f"il messaggio decriptato è: {decrp}")