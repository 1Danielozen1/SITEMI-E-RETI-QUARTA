from math import sqrt

triangolo = [(1.5,3.6),(-1.0,0.0),(5.1,4.3)]

AB = sqrt((triangolo[1][0]-triangolo[0][0])**2+(triangolo[1][1]-triangolo[0][1])**2) 
BC = sqrt((triangolo[2][0]-triangolo[1][0])**2+(triangolo[2][1]-triangolo[1][1])**2) 
AC = sqrt((triangolo[2][0]-triangolo[0][0])**2+(triangolo[2][1]-triangolo[0][1])**2) 
perimetro = AB+BC+AC
area = sqrt((perimetro/2)*(AC - AB))
print(f"AB={AB:.2f}\nBC={BC:.2f}\nAC={AC:.2f}")