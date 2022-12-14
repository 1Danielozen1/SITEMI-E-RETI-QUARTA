x = [0,1,2,3,4,5,6,7,8]
b = len(x)//2
y = x[:b]
z = x[b:]
a = [5]
y = y+a
print(f'{x}\n{y}\n{z}')