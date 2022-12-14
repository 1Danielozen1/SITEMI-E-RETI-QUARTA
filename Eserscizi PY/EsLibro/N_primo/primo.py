
"""
def primo(n,a):
    b = False
    cont = 0
    while cont < n-a and b == False:
        if(n % a == int(0)):
          b = True
          a = a+1
        else:
          a = a+1
    cont += 1
    return b
"""
def primo(n):
    cont = 0
    for i in range(2,int(n**0.5)+1):
        if(n % i == 0):
         return True
    return False


n = int(input('Inserisci un numero: '))
a = 2
b  = primo(n)

if (b == True):
    print('Il numero non è primo.')
else:
    print('Il numero è primo.')

