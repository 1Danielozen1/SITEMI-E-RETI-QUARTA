import random

f = open("casuali.txt","w")
l_Ali = []
l_Bob = []

l_Ali=[random.randint(1,6) for _ in range(0,10)]
l_Bob=[random.randint(1,6) for _ in range(0,10)]

#for i in range(10):
 #   f.write(f"{l_Ali[i]},{l_Bob[i]}")
    
for a,b in zip(l_Ali,l_Bob):
    f.write(f"Ali: {a}      Bob: {b}\n")

f.close()