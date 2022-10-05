e,d = 2,5 #assegnazione multipla.
a = 10
b = 24
print(f'\na = {a}\nb = {b}')
print(f'e = {e}\nd = {d}')
a,b = b,a
e,d = d,e
print(f'\nNuovi valori:\na = {a}\nb = {b}')
print(f'Nuovi valori:\ne = {e}\nd = {d}\n')