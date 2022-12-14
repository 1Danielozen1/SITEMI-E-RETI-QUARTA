
def nome(a):
    if(a[0] == 'G' or a[0] == 'g' or a[0] == 'h' or a[0] == 'H'):
        return True
    return False

l = ["Gauss","Conway","Eulero","Hilbert"]
l_gh = [parola for parola in l if nome(parola)]
print(l_gh)
print(l)