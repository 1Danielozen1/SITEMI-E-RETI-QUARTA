lista = [110, 113, 35, 53, 43, 214]
max = lista[0]
min = lista[0]
for elemento in lista[1:]:
    if max < elemento:
        max = elemento
    else:
        pass
    if min > elemento:
        min = elemento
    else:
        pass

print(f"Il massimo è:{max}\nIl minimo è:{min}")
