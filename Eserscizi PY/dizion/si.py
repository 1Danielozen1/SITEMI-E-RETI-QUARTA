"""
dizionario={'w':'avanti','a':'sinistra','s':'indietro','d':'destra','i':'avanti','j':'sinistra','k':'indietro','l':'destra'}
for k in dizionario:
    print(f'{k} = {dizionario[k]}')

comando = 'avanti'
l =[]
for indice,azione in dizionario.items():
    if (azione == comando):
        l.append(indice)

print(f'{l}')
"""
l = ['ciao',print,1,3.24]
for indice,elemnto in enumerate(l):
    print(indice,elemnto)
indice = 0
for elemnto in l:
    print(indice,elemnto)
    indice +=1