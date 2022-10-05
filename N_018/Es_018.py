n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
l= [n1**2+n2**2,(n1+n2)**2,n1**2-n2**2,(n1-n2)**2]
print(f'La somma dei quadrati è di {l[0]}')
print(f'Il quadrato della somma è di {l[1]}')
print(f'La differenza dei quadrati è di {l[2]}')
print(f'Il quadrato della differenza è di {l[3]}')