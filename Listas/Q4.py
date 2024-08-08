x = []
y = []
z = []
aux = 4

for i in range (5):
    x.append(int(input(f'Digite o {i+1}° valor: ')))
    
for i in range (5):
    y.append(int(input(f'Digite o {i+1}° valor da 2ª lista: ')))
    
for i in range (5):
    z.append(x[i] * y[aux])
    aux -= 1
    
print(z)